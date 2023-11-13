#!/usr/bin/python3
"""prints alphabets in lowercase apart from letter 'q' and 'e' """
for character in range(97, 123):
    if chr(character) != 'q' and chr(character) != 'e':
        print("{}".format(chr(character)), end="")
