#!/usr/bin/bash

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
        height(setter) - Setter method that sets the height
    """

    def __init__(self, width=0, height=0):
        """Initializes the attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width"""
        return __width

    @width.setter
    def width(self, value):
        """sets the width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return __height

    @width.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
