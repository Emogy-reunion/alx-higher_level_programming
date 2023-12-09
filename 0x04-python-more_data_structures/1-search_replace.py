#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list."""
    copy_list = []
    for x in range(len(my_list)):
        if my_list[x] == search:
            copy_list.append(replace)
        else:
            copy_list.append(my_list[x])
    return copy_list
