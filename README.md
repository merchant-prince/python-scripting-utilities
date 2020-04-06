# Scripting Utilities

![Project status](https://img.shields.io/badge/status-active-brightgreen?&style=flat-square)
&nbsp;&nbsp;&nbsp;&nbsp;
![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/merchant-prince/python-scripting-utilities?label=version&style=flat-square)
&nbsp;&nbsp;&nbsp;&nbsp;
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/harivansh-scripting-utilities?style=flat-square)
&nbsp;&nbsp;&nbsp;&nbsp;
![PyPI - Wheel](https://img.shields.io/pypi/wheel/harivansh-scripting-utilities?style=flat-square)
&nbsp;&nbsp;&nbsp;&nbsp;
![GitHub](https://img.shields.io/github/license/merchant-prince/python-scripting-utilities?style=flat-square)

This package consists of several utilities which are commonly used in my python
scripts.

## Installation

To install this package through pip, run the following:

```sh
pip install harivansh-scripting-utilities
```

## Usage

The following classes are available in this package:

### ChangeDirectory

This is a context manager used to change directory.

```python
from scripting_utilities import ChangeDirectory

# e.g.: currently in /tmp

with ChangeDirectory("innerdirectory"):
    # currently in /tmp/innerdirectory
    dosomething()

# back to /tmp
```

### Print

This is a utility class used to print messages to the standard output.

```python
from scripting_utilities import Print

Print.success("This is a success message.")
Print.info("This is an info message.")
Print.warning("This is a warning message.")
Print.error("This is an error message.")

Print.eol(4) # prints 4 EOLs

Print.ok() # prints: ...Ok
Print.fail() # prints: ...Failed
```

## Building

To build a **tar** and **whl** version of the package, ```cd``` into the
root project directory, and run the following:

```sh
# setup venv
python3 -m venv .venv

# activate venv
source ./.venv/bin/activate

# upgrade pip
pip install --upgrade pip

# install the necessary packages
python3 -m pip install --upgrade setuptools twine wheel

# remove the dist files if present
rm -rf build dist harivansh_scripting_utilities.egg-info

# generate the dist files
python3 setup.py sdist bdist_wheel

# upload to pypi
python3 -m twine upload dist/*

#   username: __token__
#   password: pypi-api-token
```

## Testing

To run the tests, ```cd``` into the root project directory, and run the
following:

```sh
python -m unittest discover
```
