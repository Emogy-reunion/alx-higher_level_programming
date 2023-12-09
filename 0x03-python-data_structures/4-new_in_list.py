#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replaces an element in a list
    """
    copy = my_list.copy()
    if idx > len(my_list) - 1 or idx < 0:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
