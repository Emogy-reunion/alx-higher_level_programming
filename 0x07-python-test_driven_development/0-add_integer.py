#!/usr/bin/env python3
"""functionthat sdds two integers"""


def add_integer(a, b=98):
    """
    para a: first integer
    param b: second number
    return: sum
    """

    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b
