# GWF target group

This Python package provides a convenient way for automatically generating
systematic output filenames for your GWF jobs. This will make defining your GWF
jobs a good deal terser. Compare this:

```
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

