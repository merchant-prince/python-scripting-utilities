import os


class ChangeDirectory:
    """
    This class is a context manager to change directory.
    """

    def __init__(self, newpath):
        """
        Class constructor.

        Args:
            _newpath (str): The new path to cd into.
        """

        self._oldpath = os.getcwd()
        self._newpath = newpath


    def __enter__(self):
        """
        Change directory when the context is activated.
        i.e. within the body of the associated 'with'.
        """

        os.chdir(self._newpath)


    def __exit__(self, etype, value, traceback):
        """
        Return to the old directory when the context is exited.
        i.e. when breaking out of the body of the associated 'with'.
        """

        os.chdir(self._oldpath)
