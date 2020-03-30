import os
import unittest
from scripting_utilities.cd import ChangeDirectory


class TestChangeDirectory(unittest.TestCase):

    def test_changes_directory(self):
        currentPath = os.getcwd()
        newPath = '/tmp'

        self.assertNotEqual(currentPath, newPath)

        with ChangeDirectory(newPath):
            self.assertEqual(os.getcwd(), newPath)

        self.assertEqual(os.getcwd(), currentPath)
