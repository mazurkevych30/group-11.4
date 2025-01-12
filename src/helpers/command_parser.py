"""
This module provides utility functions for parsing user input in a command-line interface (CLI).
"""

def parse_input(user_input: str):
    """
    Parse the user's input into a command and arguments.

    Args:
        user_input (str): The input entered by the user.

    Returns:
        tuple: A tuple containing the command and its arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args
