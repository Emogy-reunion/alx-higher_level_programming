#!/usr/bin/python3
"""
    method: lookup - returns a list of available attributes
        and methods ofan object
"""


def lookup(obj):
    """returns an object's methods and attributes"""
    return dir(obj)
