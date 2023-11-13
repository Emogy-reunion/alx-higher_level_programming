#!/usr/bin/python3

def remove_char_at(str, n):
    """creates a copy of a string removing the character at the 'n' position"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
