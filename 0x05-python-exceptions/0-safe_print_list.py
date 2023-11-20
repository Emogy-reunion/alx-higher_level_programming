#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print all the elememts of a list.

    Args:
        my_list: contains the elements to print
        x: number of elements in the list
    Returns:
        no of printed elements
    """
    printed = 0
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end="")
            printed += 1
        except IndexError:
            break
    print("")
    return (printed)
