# Python Shell Utils

This package consists of several utilities which are commonly used in my
scripts.


## Installation

To install this package through pip, run the following:

```
pip install -e git+https://github.com/merchant-prince/python-scripting-utilities#egg=scripting-utilities
```


## Usage

To use this package, simply ```import``` it in your python scripts.

```python
from scripting_utilities.print import Print
from scripting_utilities.cd import ChangeDirectory
from scripting_utilities.skeleton import CreateSkeleton

...
```

## Testing

To run the tests, ```cd``` into the root project directory, and run the following:

```
python -m unittest discover
```
