#!/usr/bin/python3
"""handles reading data from a file"""


def read_file(filename=" "):
    """
    Args:
        :filename: path to the file
    """
    with open(filename, "r", encoding='utf-8') as file:
        data = file.read()
        print(data, end=" ")
