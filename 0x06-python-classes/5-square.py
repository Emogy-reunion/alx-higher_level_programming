#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): value of a side of square
    """
    def __init__(self, size=0):
        """initializes the an instance of Square class
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """finds the square's area
        Returns:
            The area
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size, gets the value of __size
        Returns:
            The value of a side of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size, sets the value of __size
        Args:
            value (int): value of a side of the square
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

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
