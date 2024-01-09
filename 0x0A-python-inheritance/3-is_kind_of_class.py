#!/usr/bin/python3
"""class type checking"""


def is_kind_of_class(obj, a_class):
    """
    param obj: object to check
    param a_class: class to compare against
    Returns:
        True - if object is an instance of class or its subclass
        False - if otherwise
    """
    return isinstance(obj, a_class)
