# ContainedENV

## Description

This project is meant to provide utilities for writing out configuration files
based on environment variables.  Lots of projects seem to be implementing this
on their own (Elasticsearch/Grafana), but it would be nice to have one thing
that works for them all...so...here we go!

## Usage

Set your environment variables with a shared prefix.  Section headers should be
followed by a double underscore `__`

Example:
```
$ export MYPREFIX_foo__bar=baz
$ containedenv-config-writer.py -p MYPREFIX_
[foo]
bar = baz
```

Check out the help text for current usage info too:

```
usage: containedenv-config-writer.py [-h] -p PREFIX [-f {ini,json}]
                                     [-o OUTPUT_FILE] [-r REFERENCE_FILE]

Convert environment variables in to a configuration file

optional arguments:
  -h, --help            show this help message and exit
  -p PREFIX, --prefix PREFIX
                        Prefix of env vars to parse
  -f {ini,json}, --format {ini,json}
                        Output file format
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        Outfile file path
  -r REFERENCE_FILE, --reference-file REFERENCE_FILE
                        Load this reference file for existing/hard coded
                        values
```
