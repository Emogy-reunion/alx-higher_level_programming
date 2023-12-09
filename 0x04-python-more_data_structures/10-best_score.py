#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    return_key = list(a_dictionary.keys())[0]
    big = a_dictionary[return_key]
    for b, k in a_dictionary.items():
        if k > big:
            big = k
            return_key = b
    return (return_key)
