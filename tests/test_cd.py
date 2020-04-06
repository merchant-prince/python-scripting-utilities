import os
from unittest import TestCase
from scripting_utilities import ChangeDirectory


class TestChangeDirectory(TestCase):


    def test_changes_directory(self):
        currentPath = os.getcwd()
        newPath = '/tmp'

        self.assertNotEqual(currentPath, newPath)

        with ChangeDirectory(newPath):
            self.assertEqual(os.getcwd(), newPath)

        self.assertEqual(os.getcwd(), currentPath)
