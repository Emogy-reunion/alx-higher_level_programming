#!/usr/bin/python3
"""a class inheriting fromanother class"""


class Myclass(list):
    """inherits the list class"""

    def __init__(self):
        """initializes attributes"""
        super().__init__()

    def print_sorted(self):
        """sorts and prints the sorted list"""
        sort_list = sort(self)
        print(sort_list)
