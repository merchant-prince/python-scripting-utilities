import os


class cd:
    """
    This class is a context manager to change directory.
    """

    def __init__(self, newpath):
        self.oldpath = os.getcwd()
        self.newpath = newpath


    def __enter__(self):
        os.chdir(self.newpath)


    def __exit__(self, etype, value, traceback):
        os.chdir(self.oldpath)
