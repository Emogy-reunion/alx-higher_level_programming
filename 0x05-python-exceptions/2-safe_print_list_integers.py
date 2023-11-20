#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x list elements
    Args:
        my_list: list containing elements we are supposed to print
        x: no of elements to print
    Returns:
        no of printed elements
    """
    printed = 0
    for k in range(0, x):
        try:
            print("{:d}".format(my_list[k]), end="")
            printed += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (printed)
