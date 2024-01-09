#!/usr/bin/python3
"""utility function for class checking"""


def inherits_from(obj, a_class):
    """
    param obj: object to check
    param a_class: class to compare against
    Returns:
        True - True if the object is an instance of a class 
        that inherited (directly or indirectly) from the
        specified class ; otherwise False.
        False - if otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
