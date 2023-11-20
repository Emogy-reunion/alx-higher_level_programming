#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """
    Prints an integer
    Args:
        value: The integer to be printed.

    Returns:
        If a TypeError/ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
