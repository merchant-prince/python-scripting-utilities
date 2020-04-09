import os
from unittest import TestCase
from scripting_utilities import helpers


class TestHelpers(TestCase):
    def test_cd_changes_directory_to_the_specified_destination(self):
        old_path = os.getcwd()
        new_path = '/tmp'

        self.assertNotEqual(old_path, new_path)

        with helpers.cd(new_path):
            self.assertEqual(os.getcwd(), new_path)

        self.assertEqual(os.getcwd(), old_path)
