#!/usr/bin/python3
"""handles reading data from a file"""


def read_file(filename=" "):
    """
    param file_name: path to the file
    """
    with open(filename, "r", encoding='UTF-8') as file:
        data = file.read()
        print(data, end=" ")
