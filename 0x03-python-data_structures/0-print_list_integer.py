#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    prints all integers of a list
    """
    for k in range(len(my_list)):
        print("{:d}".format(my_list[k]))
