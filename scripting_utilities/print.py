class Colors:
    """
    This is a utility class to store the color codes used in the Print class.

    Attributes:
        CODE (dict): The color codes used throughout this class.
    """

    CODE = {
            "RED_SINDOOR": 9,
            "CHARTREUSE": 82,
            "CYAN": 4,
            "YELLOW": 220,
            "RESET": 0
    }


    def _create(self, colorCode):
        """
        Format a terminal line to accept the specified color codes.

        Args:
            colorCode (str): The terminal colors to use in the formatting.

        Returns:
            str: The formatted string.
        """

        CSI = "\033["
        END = "m"

        return f"{CSI}{colorCode}{END}"


    def _message(self, colorCode):
        """
        Format the terminal line to use the specified foreground color.

        Args:
            colorCode (str): The terminal color to use in the foreground.

        Returns:
            str: The formatted message string.
        """

        FOREGROUND = "40;38;5"

        return f"{FOREGROUND};{colorCode}"


    def _banner(self, colorCode):
        """
        Format the terminal line to use the specified background color.

        Args:
            colorCode (str): The terminal color to use in the background.

        Returns:
            str: The formatted banner string.
        """

        BACKGROUND = "30;48;5"

        return f"{BACKGROUND};{colorCode}"


    def __getattr__(self, name):
        """
        Returns a color-formatted line.

        Args:
            name (str):
                A string depicting the color-type and the display-type of the
                string to format.
                The color-type can be one of:
                    * SUCCESS
                    * INFO
                    * WARNING
                    * ERROR
                The display-type can be one of:
                    * BANNER
                    * MESSAGE

                It should be separated by an underscore and ordered as follows:
                    [color-type]_[display-type] --> e.g.: "SUCCESS_BANNER"

                Except when the RESET value is required.

        Returns:
            str: A color-coded string.

        Raises:
            ValueError: If the provided 'name' is invalid.
        """

        tokens = name.split("_")

        if len(tokens) == 1:
            if tokens[0] == "RESET":
                return self._create(Colors.CODE["RESET"])

        elif len(tokens) == 2:
            colorType, displayType = tokens

            if displayType == "BANNER":
                if colorType == "SUCCESS":
                    return self._create(self._banner(Colors.CODE["CHARTREUSE"]))

                elif colorType == "INFO":
                    return self._create(self._banner(Colors.CODE["CYAN"]))

                elif colorType == "WARNING":
                    return self._create(self._banner(Colors.CODE["YELLOW"]))

                elif colorType == "ERROR":
                    return self._create(self._banner(Colors.CODE["RED_SINDOOR"]))

            elif displayType == "MESSAGE":
                if colorType == "SUCCESS":
                    return self._create(self._message(Colors.CODE["CHARTREUSE"]))

                elif colorType == "INFO":
                    return self._create(self._message(Colors.CODE["CYAN"]))

                elif colorType == "WARNING":
                    return self._create(self._message(Colors.CODE["YELLOW"]))

                elif colorType == "ERROR":
                    return self._create(self._message(Colors.CODE["RED_SINDOOR"]))

        raise ValueError(f"{name} is not a valid attribute")




class Print:
    """
    This class is used to pretty-print messages.

    Attributes:
        Color (Colors): The Colors helper class.
    """

    Color = Colors()

    @staticmethod
    def success(message):
        """
        Print a coloured success-message.

        Args:
            message (str): The message to print.
        """

        print(Print._line(Print.Color.SUCCESS_BANNER, "Success", Print.Color.SUCCESS_MESSAGE, message), end='')


    @staticmethod
    def info(message):
        """
        Print a coloured info-message.

        Args:
            message (str): The message to print.
        """

        print(Print._line(Print.Color.INFO_BANNER, "Info", Print.Color.INFO_MESSAGE, message), end='')


    @staticmethod
    def warning(message):
        """
        Print a coloured warning-message.

        Args:
            message (str): The message to print.
        """

        print(Print._line(Print.Color.WARNING_BANNER, "Warning", Print.Color.WARNING_MESSAGE, message), end='')


    @staticmethod
    def error(message):
        """
        Print a coloured error-message.

        Args:
            message (str): The message to print.
        """

        print(Print._line(Print.Color.ERROR_BANNER, "Error", Print.Color.ERROR_MESSAGE, message), end='')


    @staticmethod
    def ok():
        """
        Print a success-colored ok-string.
        """

        print(f"{Print.Color.SUCCESS_MESSAGE} ...Ok {Print.Color.RESET}", end='')


    @staticmethod
    def fail():
        """
        Print an error-colored fail-string.
        """

        print(f"{Print.Color.ERROR_MESSAGE} ...Failed {Print.Color.RESET}", end='')


    @staticmethod
    def eol(count=1):
        """
        Print the specified count of end-of-line characters.

        Args:
            count (int): The number of EOLs to print.
        """

        print('\n' * count, end='')


    @staticmethod
    def _line(headerColor, header, messageColor, message):
        """
        Return a prettified line.

        Args:
            headerColor (str): The terminal color used to format the header.
            header (str): The message to add to the header.
            messageColor (str): The terminal color used to format the message.
            message (str): The message to prettify.

        Returns:
            str: The color-formatted line.
        """

        return f"{Print._header(headerColor, header)}{Print._message(messageColor, message)}"


    @staticmethod
    def _header(color, header):
        """
        Return a prettified string of the header.

        Args:
            color (str): The terminal color used to format the header.
            header (str): The message to add to the header.

        Returns:
            str: The color-formatted header string.
        """

        return f"{color} {header}: {Print.Color.RESET}"


    @staticmethod
    def _message(color, message):
        """
        Return a prettified string of the message.

        Args:
            color (str): The terminal color used to format the message.
            message (str): The message to prettify.

        Returns:
            str: The color-formatted message string.
        """

        return f"{color}\ue0b0 {message} {Print.Color.RESET}"
