class Colors:
    """
    This is a utility class to store the color codes used in the Print
    class.
    """

    CODE = {
            "RED_SINDOOR": 9,
            "CHARTREUSE": 82,
            "CYAN": 4,
            "YELLOW": 220,
            "RESET": 0
    }


    def __create(self, colorCode):
        CSI = "\033["
        END = "m"

        return f"{CSI}{colorCode}{END}"


    def __message(self, colorCode):
        FOREGROUND = "40;38;5"

        return f"{FOREGROUND};{colorCode}"


    def __banner(self, colorCode):
        BACKGROUND = "30;48;5"

        return f"{BACKGROUND};{colorCode}"


    def __getattr__(self, name):
        tokens = name.split("_")

        if len(tokens) == 1:
            if tokens[0] == "RESET":
                return self.__create(Color.CODE["RESET"])

        elif len(tokens) == 2:
            colorType, displayType = tokens

            if displayType == "BANNER":
                if colorType == "SUCCESS":
                    return self.__create(self.__banner(Color.CODE["CHARTREUSE"]))

                elif colorType == "INFO":
                    return self.__create(self.__banner(Color.CODE["CYAN"]))

                elif colorType == "WARNING":
                    return self.__create(self.__banner(Color.CODE["YELLOW"]))

                elif colorType == "ERROR":
                    return self.__create(self.__banner(Color.CODE["RED_SINDOOR"]))

            elif displayType == "MESSAGE":
                if colorType == "SUCCESS":
                    return self.__create(self.__message(Color.CODE["CHARTREUSE"]))

                elif colorType == "INFO":
                    return self.__create(self.__message(Color.CODE["CYAN"]))

                elif colorType == "WARNING":
                    return self.__create(self.__message(Color.CODE["YELLOW"]))

                elif colorType == "ERROR":
                    return self.__create(self.__message(Color.CODE["RED_SINDOOR"]))

        raise ValueError(f"{name} is not a valid attribute")




Color = Colors()




class Print:
    """
    This class is used to pretty-print messages
    """

    @staticmethod
    def success(message):
        """Prints a coloured success message"""

        print(Print.__line(Color.SUCCESS_BANNER, "Success", Color.SUCCESS_MESSAGE, message), end='')


    @staticmethod
    def info(message):
        """Prints a coloured info message"""

        print(Print.__line(Color.INFO_BANNER, "Info", Color.INFO_MESSAGE, message), end='')


    @staticmethod
    def warning(message):
        """Prints a coloured warning message"""

        print(Print.__line(Color.WARNING_BANNER, "Warning", Color.WARNING_MESSAGE, message), end='')


    @staticmethod
    def error(message):
        """Prints a coloured error message"""

        print(Print.__line(Color.ERROR_BANNER, "Error", Color.ERROR_MESSAGE, message), end='')


    @staticmethod
    def ok():
        """Prints a coloured ok message"""

        print(f"{Color.SUCCESS_MESSAGE} ...Ok {Color.RESET}", end='')


    @staticmethod
    def fail():
        """Prints a coloured failure message"""

        print(f"{Color.ERROR_MESSAGE} ...Failed {Color.RESET}", end='')


    @staticmethod
    def eol(count=1):
        """Prints an end of line character"""

        print('\n' * count, end='')


    @staticmethod
    def __line(headerColor, header, messageColor, message):
        """Returns a pretified line"""

        return f"{Print.__header(headerColor, header)}{Print.__message(messageColor, message)}"


    @staticmethod
    def __header(color, header):
        """Returns a pretty-string of the header"""

        return f"{color} {header}: {Color.RESET}"


    @staticmethod
    def __message(color, message):
        """Returns a pretty-string of the message"""

        return f"{color}\ue0b0 {message} {Color.RESET}"
