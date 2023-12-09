#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""
    new_dictionary = {}
    for x in a_dictionary:
        new_dictionary[x] = a_dictionary[x] * 2
    return new_dictionary
