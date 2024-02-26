#!/usr/bin/python3
"""defines a BaseGeometry class and class Rectangle"""


class BaseGeometry:
    """
    class to perform basi geometric operations
    """

    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates the given value

        param name: The name of the value
        param value: The value to validate
        raises TypeError: If the value is is not an integer
        raises ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name:s} must be an integer")
        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")

class Rectangle:
    """
    a represantation of a rectangle
    """

    def __init__(self, width, height):
        """initialize objects"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validatot("height", height)
        self.__height = height

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the informal  string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"
