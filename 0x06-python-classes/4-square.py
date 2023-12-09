#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Square class
    Attributes:
        __size (int): (private attribute)size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square instance
        Args:
            size (int): size of one side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the area of the square
        Returns:
            The area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter, gets the __size
        Returns:
            The size of one side of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter, sets the __size attribute
        Args:
            value (int): the value of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
