import unittest
from scripting_utilities.print import Print


class TestPrint(unittest.TestCase):

    def test_print_all(self):
        print("\n" * 2)

        self.__printSuccess()
        self.__printInfo()
        self.__printWarning()
        self.__printError()
        self.__printInfoWithFailed()
        self.__printInfoWithOk()

    def __printSuccess(self):
        print("Printing a success message with 2 EOLs:")

        Print.success("This is a success message.")
        Print.eol(2)

    def __printInfo(self):
        print("Printing an info message with 3 EOLs:")

        Print.info("This is an info message.")
        Print.eol(3)

    def __printWarning(self):
        print("Printing a warning message with 4 EOLs:")

        Print.warning("This is a warning message.")
        Print.eol(4)

    def __printError(self):
        print("Printing an error message with 5 EOLs:")

        Print.error("This is an error message.")
        Print.eol(5)

    def __printInfoWithOk(self):
        print("Printing info with an ok message:")

        Print.info("This is an info message.")
        Print.ok()
        Print.eol(2)

    def __printInfoWithFailed(self):
        print("Printing info with a failed message:")

        Print.info("This is an info message.")
        Print.fail()
        Print.eol(2)
