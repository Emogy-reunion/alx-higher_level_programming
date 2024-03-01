#!/usr/bin/python3
"""handles reading data from a file"""


def read_file(file_name=""):
    """
    param file_name: path to the file
    """
    with open(file_name, "r") as file:
        print(file.read())
