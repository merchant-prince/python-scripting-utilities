import os
from pathlib import Path
from collections.abc import Mapping
from scripting_utilities import ChangeDirectory


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

        CreateSkeleton._validate(structure)
        CreateSkeleton._create(structure)


    @staticmethod
    def _create(structure):
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
                    CreateSkeleton._create(structure)


    @staticmethod
    def _validate(structure):
        """
        Validates the directory structure provided.

        Args:
            structure (dict): The directory structure to validate.

        Raises:
            ValueError: If the given structure is invalid.
        """

        errorMessage = "The directory structure provided is ill-formed"

        if not CreateSkeleton._isValid(structure):
            raise ValueError(errorMessage)

        if isinstance(structure, Mapping):
            for name, structure in structure.items():
                if not CreateSkeleton._isValid(structure):
                    raise ValueError(errorMessage)

                CreateSkeleton._validate(structure)


    @staticmethod
    def _isValid(structure):
        """
        Checks if a given structure is valid.

        Args:
            structure (dict): The directory structure to validate.

        Returns:
            bool: True if the given structure is valid, False otherwise.
        """

        return isinstance(structure, Mapping) or isinstance(structure, str)
