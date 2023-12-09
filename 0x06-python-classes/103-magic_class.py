#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """This represents a circle object"""
    def __init__(self, radius=0):
        """Initializes the instance attributes"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """finds the area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """finds the circumference of the circle"""
        return 2 * math.pi * self.__radius
