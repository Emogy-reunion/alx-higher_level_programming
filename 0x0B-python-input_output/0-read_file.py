#!/usr/bin/python3
"""handles reading data from a file"""


def read_file(file_name=""):
    """
    param file_name: path to the file
    """
    with open(file_name, "r", encoding='UTF-8') as file:
        data = file.read()
        print(data, end=" ")
