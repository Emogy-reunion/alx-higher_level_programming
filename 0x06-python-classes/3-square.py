#!/usr/bin/python3
""" defines a Class square """


class Square:
    """ a class Square with private instance attribute size """

    def __init__(self, size=0):
        """
        method that initializes square
        Args:
            size: size of one side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        calculates area of the square
        Returns:
            the area
        """

        return self.__size ** 2
