#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """class to represents a square
    Attributes:
        __size (int): (private attribute) size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): the size of one side of the square
        Returns: Nothing
        """
        self.__size = size
