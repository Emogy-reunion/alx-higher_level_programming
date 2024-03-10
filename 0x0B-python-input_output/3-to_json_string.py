#!/usr/bin/python3
"""
it contains function that converts string to  the JSON
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
