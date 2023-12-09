#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    prints all integers in  list in reverse order
    """
    if my_list:
        my_list.reverse()
        for k in range(len(my_list)):
            print("{:d}".format(my_list[k]))
