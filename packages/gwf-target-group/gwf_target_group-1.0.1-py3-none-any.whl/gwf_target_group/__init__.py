#!/usr/bin/env python3

"""
Provide an even higher-level API to gwf.

gwf is great for file dependency resolution. But you still have to define the
file paths yourself and that's quite a bit of manual work. This API tries to
automatically give sensible names to files and directories for you, so that you
can focus on crafting shell commands that produce results and feed into each
other.


The idea is to create an initial gwf workflow object like so:

>>> gwf = Workflow() # insert any parameters you need to the constructor

And then wrap it by specifying where result files should go:

>>> tg = TargetGroup( gwf, 'group_name', 'output/prefix/directory/' )

We just defined `tg` which we can use to define individual targets like so:

>>> tg(
...     'suffix_of_target', # target name will be 'group_name.suffix_of_target'
...     'scripts/foo.sh {infile1} {infile2} {outfile1.txt} {outfile2.pdf}',
...     infile1 = 'path/to/infile1',
...     infile2 = 'path/to/infile2',
... )
{'outfile1': 'output/prefix/directory//suffix_of_target/outfile1.txt', 'outfile2': 'output/prefix/directory//suffix_of_target/outfile2.pdf'}

The first argument is always the suffix to the target name that should be defined
The second argument is an f-string without the f in the beginning to prevent it from evaluation
Any further arguments define input files that correspond to slots in the f-string
Any missing arguments to the f-string are treated as output files and the API will generate appropriate file names for them.

Also note that you can include file suffixes for the output files. The naming API will automatically use these output suffixes.
The return value above contains the paths to all files that should be produced by this target.

Afterwards you will be able to access the output file paths by combining the "suffix_of_target" and the names of the output files:

>>> tg.suffix_of_target.outfile1 # note the lack of a file extension
'output/prefix/directory//suffix_of_target/outfile1.txt'
>>> tg.suffix_of_target.outfile2
'output/prefix/directory//suffix_of_target/outfile2.pdf'

And then you can use these output files in the definition of new targets:

>>> tg(
...     'count_genes',
...     'wc -l {gene_list} > {gene_count}',
...     gene_list = tg.suffix_of_target.outfile1 # using output file from previous step
... )
{'gene_count': 'output/prefix/directory//count_genes/gene_count'}

If you need to use curly braces {} in the definition of the shell command, you can escape them by prefixing them with the same curly brace:

>>> tg(
...    'add_columns',
...    "awk '{{print( $1 + $2 )}} {column_file} > {sumfile.txt}",
...    column_file = "my_file" )
{'sumfile': 'output/prefix/directory//add_columns/sumfile.txt'}
>>> gwf.targets[ 'group_name.add_columns' ].spec
"awk '{print( $1 + $2 )} my_file > output/prefix/directory//add_columns/sumfile.txt"


    
"""

from typing import List, Dict
from types import SimpleNamespace
import re
from os.path import dirname
from  os import makedirs

from gwf import Workflow
from gwf.utils import is_valid_name

def _remove_file_extensions_in_format_string( fmt_string ):
    """
    Remove all file extensions from inside f-string slots.

    >>> fun = _remove_file_extensions_in_format_string
    >>> fun( '' )
    ''
    >>> fun( '{bla.txt}' )
    '{bla}'
    >>> fun( ' {bla.txt} ' )
    ' {bla} '
    >>> fun( ' a{{bla.txt}}b ' )
    ' a{{bla.txt}}b '
    >>> fun( ' {foo.gz} {bar.txt} {bang}' )
    ' {foo} {bar} {bang}'
    >>> fun( '{{bla.txt}' ) # this is a bad f-string, but let's parse it anyway
    '{{bla.txt}'
    >>> fun( '{blubb.txt:.2f}' )
    '{blubb:.2f}'
    >>> fun( 'hello {world.tar.gz} {goodbye.world}!' )
    'hello {world} {goodbye}!'
    >>> fun( '{bla.txt{}' )
    Traceback (most recent call last):
    ...
    ValueError: Bad "{" in substring: {bla{
    """
    result = []
    in_brace = False
    in_dot = False
    in_colon = False
    for c in fmt_string:
        if c == '{':
            if in_dot or in_colon: # this { should not be here
                raise ValueError( 'Bad "{" in substring: %s{' % ( ''.join( result ) ) )

            if in_brace and result[ -1 ] == '{': # it is an escape sequence
                in_brace = False # don't treat things special any more
                # in_dot = in_colon = False is implicit
            else:
                in_brace = True # Now we are looking for file extensions to remove
        elif c == '}':
            in_brace = False
            in_dot = False
            in_colon = False
        elif in_colon:
            pass # we accept everything until the next }
        elif c == ':' and in_brace: # advanced string formatting. We want to keep that intact
            in_colon = True
            in_dot = False # given the ordering of if-else, this is implicit
        elif c == '.' and in_brace:
            in_dot = True # we drop everything until the next } or :
            continue
        elif in_dot:
            continue # we need a closing } to start recording again
        result.append( c )
    return ''.join( result )

def _generate_filename( target_name, var_name, outdir_prefix ):
    """
    Generate a filename based on the input parameters:

    output_prefix + target_name + var_name

    >>> fun = _generate_filename
    >>> fun( 'foo', 'bar.tar.gz', 'my_results' )
    'my_results/foo/bar.tar.gz'
    """
    return f'{outdir_prefix}/{target_name}/{var_name}'

def _extract_inputs_and_outputs( target_name, command_string, outdir_prefix, keywords ):
    """
    Determine the input and output parmeters for a given command_string.


    >>> fun = _extract_inputs_and_outputs
    >>> fun( 'foo', 'make {input} {output.txt}', 'results', { 'input': 'bar' } )
    ({'input': 'bar'}, {'output': 'results/foo/output.txt'}, 'make {input} {output}')
    """
    inputs = {} # input_name -> input_file
    outputs = {} # output_name -> output_file
    seen_inputs = set()
    for match in re.finditer('{[^}]*}', command_string ): # find {foo:stringspec}
        var_name, *advanced_formatting = match.group( 0 )[ 1:-1 ].split( ':' ) # and extract foo
        if var_name.startswith( '{' ): # it's an {{ escape sequence
            continue # this is not meant for us
        if var_name in keywords:
            inputs[ var_name ] = keywords[ var_name ]
            seen_inputs.add( var_name )
        else:
            stem = var_name.split( '.' )[ 0 ]
            outputs[ stem ] = _generate_filename( target_name, var_name, outdir_prefix )
    
    for absent_input in keywords.keys() - seen_inputs:
        raise ValueError( f'The keyword »{absent_input}« was provided but is not in the format string' )

    new_command_string = re.sub( '\n *',
                                 ' ',
                                 _remove_file_extensions_in_format_string( command_string ) ).strip()
    #print( new_command_string )

    output_directories = { dirname( dir ) for dir in outputs.values() }
    for dir in output_directories:
        makedirs( dir, exist_ok = True )

    return inputs, outputs, new_command_string



class TargetGroup:
    def __init__( self, gwf, label_prefix, outdir_prefix ):
        """
        A group of gwf targets with a common target-name-prefix and a common
        output file prefix.

        Objects of this class will also have an attribute for every gwf target
        that is defined with this target group. That attribute will then have
        one attribute for every output file. This way you can easily pass paths
        to files from one target to another.


        >>> gwf = Workflow()
        >>> tg = TargetGroup( gwf, 'test_jobs', 'results' )
        >>> tg(
        ...     'job1',
        ...     'make-things {input1} {input2} {output.tsv}',
        ...     input1 = 'foo.txt',
        ...     input2 = 'bar.txt'
        ... )
        {'output': 'results/job1/output.tsv'}
        >>> tg(
        ...     'job2',
        ...     'make-more-things {my_input} {my_output.tar.gz}',
        ...     my_input = tg.job1.output
        ... )
        {'my_output': 'results/job2/my_output.tar.gz'}


        """
        self._gwf = gwf
        self._label_prefix = label_prefix
        self._outdir_prefix = outdir_prefix
        # and every `target_name` will become an attribute mapping to {output_name->filename}


    def __call__( self, target_name, command_string, gwf_options = None, **keywords ):
        """
        Use objects of this class like a function to define new gwf targets.

        :param target_name: suffix of target's name (prefix is `label_prefix`)
        :param command_string: Unevaluated f-string with slots for input files and output files
        :param gwf_options: Arguments passed to gwf.target()
        :param keywords: Paths to input files. The keys must correspond to slots in the command_string
        :returns: A dictionary of output files
        """

        full_target_name = self._label_prefix + '.' + target_name

        if target_name.startswith( '_' ):
            raise ValueError( f'The target_name {target_name} must not start with an "_". target_name=' + target_name )
        elif '.' in target_name:
            raise ValueError( f'The target_name {target_name} contains a dot (.)' )
        elif not is_valid_name( full_target_name ):
            raise ValueError( f"The target name \"{full_target_name}\" does not conform to gwf's naming conventions https://docs.gwf.app/reference/api/#gwf.Target" )

        for k, v in keywords.items():
            if type( v ) is not str:
                raise TypeError( f'Parameter `{k}` being passed to `{self._label_prefix}.{target_name}()` must be a string' )

        inputs, outputs, new_command_string = _extract_inputs_and_outputs(
            target_name,
            command_string,
            self._outdir_prefix,
            keywords
        )

        cmd = new_command_string.format( **inputs, **outputs )
        #print( cmd )
        self._gwf.target(
            full_target_name,
            inputs = list( inputs.values() ),
            outputs = list( outputs.values() ),
            **( gwf_options or {} )
        ) << cmd
        setattr( self, target_name, SimpleNamespace( **outputs ) )
        return outputs

