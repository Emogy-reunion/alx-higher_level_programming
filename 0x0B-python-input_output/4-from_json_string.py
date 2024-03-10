#!/usr/bin/python3
"""
it contains function that converts json string back to an object
"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
