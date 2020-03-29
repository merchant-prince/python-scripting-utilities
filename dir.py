import os
import collections

from .ChangeDirectory import ChangeDirectory


class DirectoryStructure:
    """
    A class to create a directory structure according to the structure defined.

    Attributes
    ----------
    structure: dictionary<dictionary<...>>
        A dictionary of dictionaries representing the directory structure.

        e.g.: { "one": {
                    "eleven": {},
                    "twelve": {}
                },
                "two": {}
              }
    """
    def __init__(self, structure):
        DirectoryStructure.__checkStructure(structure)
        DirectoryStructure.__createDirectory(structure)


    @staticmethod
    def __createDirectory(structure):
        """
        This method needs to be static so that we can pass the leaves of the
        structure to itself recursively.
        """
        for directoryName, directoryContent in structure.items():
            os.mkdir(directoryName)

            with cd(directoryName):
                DirectoryStructure.__createDirectory(directoryContent)


    @staticmethod
    def __checkStructure(dictionary):
        """
        This method needs to be static so that we can pass the leaves of the
        dictionary to itself recursively.
        """
        if not isinstance(dictionary, collections.Mapping):
            raise ValueError("The directory structure provided is ill-formed")

        for directoryName, directoryContent in dictionary.items():
            if isinstance(directoryContent, collections.Mapping):
                DirectoryStructure.__checkStructure(directoryContent)
            else:
                raise ValueError("The directory structure provided is ill-formed")
