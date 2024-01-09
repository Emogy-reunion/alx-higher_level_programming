#!/usr/bin/python3
"""defines aBaseGeometry class"""


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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
