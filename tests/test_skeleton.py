import os
import shutil
import random
import string
import unittest
from scripting_utilities.cd import ChangeDirectory
from scripting_utilities.skeleton import CreateSkeleton


class TestCreateSkeleton(unittest.TestCase):

    def test_returns_true_when_valid_structure_is_provided(self):
        validStructures = [
            {},
            ""
        ]

        for structure in validStructures:
            self.assertTrue(CreateSkeleton._CreateSkeleton__isValid(structure))


    def test_returns_false_when_invalid_structure_provided(self):
        invalidStructures = [
            (),
            12,
            []
        ]

        for structure in invalidStructures:
            self.assertFalse(CreateSkeleton._CreateSkeleton__isValid(structure))


    def test_does_not_raise_exception_on_valid_structure_validation(self):
        validStructure = {
            "directory_1": {},
            "file_1": "",
            "directory_2": {
                "inner_file_1": "",
                "inner_directory_1": {},
                "inner_file_2": ""
            },
            "file_2": ""
        }

        self.assertTrue(CreateSkeleton._CreateSkeleton__validate(validStructure) is None)


    def test_raises_exceptions_on_invalid_structure_validation(self):
        invalidStructure = {
            "directory_1": {},
            "file_1": "",
            "directory_2": {
                "inner_file_1": "",
                "inner_directory_1": [],
                "inner_file_2": ""
            },
            "file_2": ()
        }

        self.assertRaises(ValueError, CreateSkeleton._CreateSkeleton__validate, invalidStructure)


    def test_creates_skeleton_if_a_valid_structure_is_provided(self):
        fileNameLength = 32
        randomDirectoryName = ''.join(random.choices(string.ascii_uppercase, k=fileNameLength))
        validStructure = {
            randomDirectoryName: {
                "directory_1": {},
                "file_1": "",
                "directory_2": {
                    "inner_file_1": "",
                    "inner_directory_1": {},
                    "inner_file_2": ""
                },
                "file_2": ""
            }
        }

        with ChangeDirectory("/tmp"):
            CreateSkeleton(validStructure)

            self.assertTrue(os.path.isdir(randomDirectoryName))

            with ChangeDirectory(randomDirectoryName):
                self.assertTrue(os.path.isdir("directory_1"))
                self.assertTrue(os.path.isfile("file_1"))
                self.assertTrue(os.path.isdir("directory_2"))

                with ChangeDirectory("directory_2"):
                    self.assertTrue(os.path.isfile("inner_file_1"))
                    self.assertTrue(os.path.isdir("inner_directory_1"))
                    self.assertTrue(os.path.isfile("inner_file_2"))

                self.assertTrue(os.path.isfile("file_2"))

            shutil.rmtree(randomDirectoryName)

            self.assertFalse(os.path.isdir(randomDirectoryName))


    def test_throws_an_exception_and_does_not_create_any_files_when_invalid_structure_provided(self):
        fileNameLength = 32
        randomDirectoryName = ''.join(random.choices(string.ascii_uppercase, k=fileNameLength))
        invalidStructure = {
            randomDirectoryName: {
                "directory_1": [],
                "file_1": "",
                "directory_2": {
                    "inner_file_1": 12,
                    "inner_directory_1": {},
                    "inner_file_2": ()
                },
                "file_2": ""
            }
        }

        with ChangeDirectory("/tmp"):
            self.assertRaises(ValueError, CreateSkeleton, invalidStructure)
            self.assertFalse(os.path.isdir(randomDirectoryName))
