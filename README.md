# `line-craft`

A simple toolkit for creating modified versions of text-based files. Changes are applied line-wise. Specifically, the software provides functionality to:  
(1) Write a version of the file where certain modifications have been applied to each line.  
(2) Write a version of the file where only lines that fulfil some condition are retained.  
(3) Write a version of the file where only a random subset of lines is retained (sampled).  


## Installation

Required: Python3.8+

```bash
# Set up virtual environemnt (recommended)
$ python3 -m venv .venv && source .venv/bin/activate && pip install --upgrade pip
$ pip install git+ssh://git@github.com/ybracke/line-craft.git
```

For developping, install dev-requirements:

```bash
pip install -r requirements-dev.txt
```


## Usage

### Python package

Example:

```python
import line_craft

infile = "example01.txt"
outfile = "example01.filtered.txt"

# condition
def longer_than_10_chars(line):
    return len(line) > 10

filter_lines(infile, outfile, longer_than_10_chars)
```

### Command-line usage

After installation, `line-craft` is available as a command line tool. As of now,
you can only use the `sample` function via this CLI. 

```bash
$ line-craft --help
# alternatively
$ python3 -m line_craft --help
```

Example:

```bash
$ line-craft --out example01.rand-4.jsonl sample -n 4 example01.jsonl 
```

