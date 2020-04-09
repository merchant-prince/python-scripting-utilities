import os
import sys
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

    def test_tmpdir_creates_a_directory_and_cds_into_it(self):
        dirname = "TEMPORARY_DIRECTORY_NAME"
        parentdir = "/tmp"
        currentdir = os.getcwd()

        self.assertFalse(os.path.isdir(f"{parentdir}/{dirname}"))

        with helpers.tmpdir(dirname, parentdir):
            self.assertEqual(f"{parentdir}/{dirname}", os.getcwd())

        self.assertEqual(currentdir, os.getcwd())

    def test_tmpdir_removes_the_temporary_directory_when_exiting_the_context(self):
        with helpers.tmpdir():
            dirname = os.getcwd()

        self.assertFalse(os.path.isdir(dirname))

    def test_capturestdout_does_not_output_any_printed_values(self):
        with helpers.capturestdout():
            print("########################################")
            print("## THIS MESSAGE SHOULD NOT BE PRINTED ##")
            print("########################################")

    def test_capturestdout_saves_any_printed_output_to_the_context_variable(self):
        output = "This is the string to be printed."

        with helpers.capturestdout() as stdout:
            print(output, end='')

        self.assertEqual(output, stdout.getvalue())

    def test_capturestdout_restores_the_stdout_buffer_when_exiting_the_context(self):
        current_stdout = sys.stdout

        with helpers.capturestdout():
            print("some value...")

        self.assertEqual(current_stdout, sys.stdout)

    def test_injectstdin_sets_the_value_of_any_input_statements_without_prompting_the_user(self):
        answer = "world"

        # we capture stdout to prevent the input prompt from printing during the test
        with helpers.capturestdout():
            with helpers.injectstdin(answer):
                input_value = input("Hello? ")

        self.assertEqual(answer, input_value)

    def test_injectstdin_restores_the_stdin_buffer_when_exiting_the_context(self):
        current_stdin = sys.stdin

        with helpers.injectstdin("some value..."):
            pass

        self.assertEqual(current_stdin, sys.stdin)
