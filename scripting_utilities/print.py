from termcolor import colored


def success(message):
    return colored(f"[ SUCCESS ]: {message}", "green")


def info(message):
    return colored(f"[ INFO ]: {message}", "blue")


def warning(message):
    return colored(f"[ WARNING ]: {message}", "yellow")


def error(message):
    return colored(f"[ ERROR ]: {message}", "red")


def ok():
    return colored("...Ok", "green")


def failed():
    return colored("...Failed", "red")
