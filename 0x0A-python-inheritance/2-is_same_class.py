#!/usr/bin/python3
"""method that checks if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """
    param obj: the object to check
    param a_class: class to compare against
    Returns:
        True - if obj is an instance of the specified class
        False- if otherwise
    """
    return (type(obj) == a_class)
