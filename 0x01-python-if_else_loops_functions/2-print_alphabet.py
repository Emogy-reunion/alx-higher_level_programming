#!/usr/bin/python3
"""it prints the ASCII alphabet in lowercase without a newline."""

for character in range(97, 123):
    print("{}".format(chr(character)), end="")
