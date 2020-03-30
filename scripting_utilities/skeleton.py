import os
from pathlib import Path
from .cd import ChangeDirectory
from collections.abc import Mapping


class CreateSkeleton:
    """
    A class to create a directory structure in the current directory depending
    on the structure defined.
    """

    def __init__(self, structure):
        """
        Class constructor.

        Args:
            structure (dict):
                The directory structure to create in the current directory.
                It is typically a dictionary of dictionaries or strings
                representing the directory structure.
                The empty dictionaries represent directories, while the strings
                represent files.

                e.g.: { "one": {
                            "eleven": {},
                            "twelve": {
                                "file.txt": "",
                                "anotherfile.jpeg": "",
                                "inner-directory": {}
                            }
                        },
                        "two.py": ""
                    }
        """

        CreateSkeleton.__validate(structure)
        CreateSkeleton.__create(structure)


    @staticmethod
    def __create(structure):
        """
        Create the provided files, and directories in the structure.

        Args:
            structure (dict): The directory structure to create in the current directory.
        """

        for name, structure in structure.items():
            if isinstance(structure, str):
                Path(name).touch()
            elif isinstance(structure, Mapping):
                os.mkdir(name)

                with ChangeDirectory(name):
                    CreateSkeleton.__create(structure)


    @staticmethod
    def __validate(structure):
        """
        Validates the directory structure provided.

        Args:
            structure (dict): The directory structure to validate.

        Raises:
            ValueError: If the given structure is invalid.
        """

        errorMessage = "The directory structure provided is ill-formed"

        if not CreateSkeleton.__isValid(structure):
            raise ValueError(errorMessage)

        if isinstance(structure, Mapping):
            for name, structure in structure.items():
                if not CreateSkeleton.__isValid(structure):
                    raise ValueError(errorMessage)

                CreateSkeleton.__validate(structure)


    @staticmethod
    def __isValid(structure):
        """
        Checks if a given structure is valid.

        Args:
            structure (dict): The directory structure to validate.

        Returns:
            bool: True if the given structure is valid, False otherwise.
        """

        return isinstance(structure, Mapping) or isinstance(structure, str)
