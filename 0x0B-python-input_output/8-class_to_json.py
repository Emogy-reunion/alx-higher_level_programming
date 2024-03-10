#!/usr/bin/python3
"""
Contains function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """returns the dictionary description with simple ds
    for JSON serialization of an object"""
    return obj.__dict__
