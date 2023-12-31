#!/usr/bin/python3

"""Aclass Rectangle representing a rectangle"""


class Rectangle:
    """
    A class representing a rectangle

    Attributes:
        height(int) - height of the rectangle
        width(int) - width of the rectangle

    methods:
        width(property) -Getter method that retrieves the width
        width(setter) - Setter method that sets the width
        height(property) - Getter method that retrieves the height
        height(setter) - Setter method that sets the height"""

    def __init__(self, width=0, height=0):
        """Initializes the attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and returns the area of the rectangle"""
        the_area = self.__width * self.__height
        return the_area

    def perimeter(self):
        """calculates and returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            the_perimeter = 2 * (self.__width + self.__height)
            return the_perimeter

    def __str__(self):
        """method to provide a string representation of rectamgle"""
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        else:
            for _ in range(self.__height):
                rectangle_str += '#' * self.__width + '\n'
            return rectangle_str.strip()

    def __repr__(self):
        """method to provide a string representation for
        recreation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """method to print a message when an instance is deleted"""
        print("Bye rectangle...")
