""""This module provides a decorator function for handling common errors in command functions."""
from colorama import init, Fore

init()

def input_error(func):
    """"Function for errors messages"""
    messages = [
        "The phone number must be 10 digits.",
        "Name is required field.",
        "Invalid email.",
        "Invalid date format. Use DD.MM.YYYY",
        "Phone number already exists"
        ]

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e) in messages:
                return Fore.RED + str(e) + Fore.RESET
            return Fore.RED + "Enter the argument for the command" + Fore.RESET
        except KeyError:
            return Fore.RED + "Not found." + Fore.RESET
        except IndexError:
            return Fore.RED + "Enter user name." + Fore.RESET
    return inner
