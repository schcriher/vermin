[![Build Status](https://travis-ci.org/netromdk/minpy.svg?branch=master)](https://travis-ci.org/netromdk/minpy)

# minpy
Concurrently detect the minimum Python version needed to run code.

Works with Python 2.7 and 3+.

It functions by parsing Python code into an abstract syntax tree (AST), which it traverses and matches against internal dictionaries of 39 modules, 79 classes/functions/constants members of modules, and 13 kwargs of functions. Including looking for v2/v3 `print expr` and `print(expr)`, `"..".format(..)`, imports (`import X`, `from X import Y`, `from X import *`), and function calls wrt. name and kwargs.

## Usage
It is fairly straightforward to use Minpy:
```
% ./minpy.py
Usage: ./minpy.py [-v|--verbose] <python source files and folders..>

% ./minpy.py minpy.py
Minimum required versions: 2.7, 3.0

% ./minpy.py examples
3.4          /path/to/git/minpy/examples/abc.py
2.7, 3.2     /path/to/git/minpy/examples/argparse.py
2.7, 3.0     /path/to/git/minpy/examples/formatv3.py
2.0          /path/to/git/minpy/examples/printv2.py
3.0          /path/to/git/minpy/examples/printv3.py

Minimum required versions: 3.4
```
