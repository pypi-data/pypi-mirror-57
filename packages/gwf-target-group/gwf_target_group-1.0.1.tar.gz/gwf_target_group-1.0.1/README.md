# gwf target group

This Python package provides a convenient way for automatically generating
systematic output filenames for your gwf jobs. This will make defining your gwf
jobs a good deal terser. Compare this:

```
from gwf import Workflow

gwf = Workflow()

foo_file = 'first_step/foo.csv' 
bar_file = 'first_step/bar.csv' 
plot_file = 'second_step/plot.png'
summary_file = 'second_step/summary.txt'

gwf.target(
    'target_group.first_step',
    inputs = [],
    outputs = [ foo_file, bar_file ],
) << f"first_step_command -f {foo_file} > {bar_file}"

gwf.target(
    'target_group.second_step',
    inputs = [ foo_file, bar_file ],
    outputs = [ plot_file, summary_file ]
) << f"second_step_command -f {foo_file} -b {bar_file} -p {plot_file} > {summary_file}"
```

to this:

```
from gwf import Workflow
from gwf_target_group import TargetGroup

gwf = Workflow()

target_group = TargetGroup( gwf, 'target_group', 'output_prefix/' )

target_group(
    'first_step',
    "first_step_command -f {foo.csv} > {bar.csv}"
) # No input files here. Only 2 output files

target_group(
    'second_step',
    "run_command -f {foo_file} -b {bar_file} -p {plot.png} > {summary.txt}",
    foo_file = target_group.first_step.foo,
    bar_file = target_group.first_step.bar
) # Two input files, two output files
```

With this package you never specify the path to the output files. Only to the
input files. And you can easily refer to the output files by using the automatic
attributes of the target group: `target_group.first_step.foo`.

## Installation

Install via pip:

```
pip install gwf_target_group
```

(or alternatively copy the `__init__.py` from this repository and save if as
`gwf_target_group.py` at a convenient location)


## Advanced usage

### Passing gwf options

If you need to fine-tune the options for a gwf job, you can use the
`gwf_options` parameter:

```
target_group(
    'my_special_processing_step',
    'do_special_things {data} > {result.tsv}',
    gwf_options = { # gwf_options is a reserved keyword
        'memory': '64g',
        'walltime': 'unlimited'
    },
    data = 'path/to/data.tsv'
)
```

This is roughly equivalent to the following gwf-only code:

```
gwf.target(
    'target_group.my_special_processing_step',
    inputs = [ 'path/to/data.tsv' ],
    outputs = [ 'path/to/result.tsv' ],
    options = {
        'memory': '64g',
        'walltime': 'unlimited'
    }
) << 'do_special_things path/to/data.tsv > path/to/result.tsv'
```

### running workflows with different datasets

Sometimes you want to do the same thing with different datasets. For example,
you might have a human and a mouse dataset that you want to analyse. Then you
can do the following:

```
def define_analysis( target_group ):
    target_group(
        'sort_genes_by_length',
        'gene_sorter --by length {genome_file} > {list}',
        genome_file = target_group.genome_file # this value was attached previously
    )
    target_group(
        'split_into_test_and_training_datasets',
        'split_list -1 list1 -2 list2 {sorted_genes}',
        sorted_genes = target_group.sort_genes_by_length.list
    )
    # more steps can be added here

human = TargetGroup( gwf, 'human', 'human_results/' )
mouse = TargetGroup( gwf, 'mouse', 'mouse_results/' )

# explicitly attach the path to the genome files to the TargetGroups
human.genome_file = 'data/genomes/human.fa'
mouse.genome_file = 'data/genomes/mouse.fa'

# and then define the analysis for both datasets
define_analysis( human )
define_analysis( mouse )
        '
```
