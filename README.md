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

This package consists of several utilities which are commonly used in my python scripts. It is available as a
[pip package](https://pypi.org/project/harivansh-scripting-utilities).

## Installation

To install this package through pip, run the following:

```sh
pip install harivansh-scripting-utilities
```

## Testing

To run the tests, ```cd``` into the root project directory, and run the following:

```sh
docker run --rm -u `id -u`:`id -g` -v "`pwd`:/application" -w "/application" python python3 -m unittest discover -s tests
```

## Building

@todo: ADD SCRIPT TO BUILD THE TAR AND WHL PACKAGES
