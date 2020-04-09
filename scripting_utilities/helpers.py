import os
import sys
import random
import shutil
import string
from io import StringIO
from contextlib import contextmanager


@contextmanager
def cd(destination):
    """
    A context manager to change directory. Mimics unix's cd.

    Args:
        destination (str): The directory to cd into.
    """

    cwd = os.getcwd()

    try:
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


@contextmanager
def tmpdir(dirname="".join(random.choices(f"{string.ascii_letters}{string.digits}_", k=64)), parentdir="/tmp"):
    """
    Create and cd into a temporary directory.
    The the created temporary directory is removed when the context is exited.

    Args:
        dirname (str):
            The name of the temporary directory to create and cd into.
        parentdir (str):
            The name of the directory where the temporary directory will be created.
    """

    with cd(parentdir):
        try:
            os.mkdir(dirname)

            with cd(dirname):
                yield
        finally:
            shutil.rmtree(dirname)


@contextmanager
def capturestdout():
    """
    Suppress the standard output and redirect it to another buffer.

    Usage:
        with suppress_stdout() as stdout:
            do_something()
            ...
        buffer_contents = stdout.getvalue()
    """

    original_stdout = sys.stdout
    sys.stdout = new_stdout = StringIO()

    try:
        yield new_stdout
    finally:
        sys.stdout = original_stdout


@contextmanager
def injectstdin(value):
    """
    Pass a string to stdin.

    Args:
        value (str): The value to pass to the standard input.
    """

    original_stdin = sys.stdin
    sys.stdin = StringIO(value)

    try:
        yield
    finally:
        sys.stdin = original_stdin
