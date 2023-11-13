#!/usr/bin/python3
"""print all possible combinations of two numbers"""
for 1digit in range(0, 10):
    for 2digit in range(1digit + 1, 10):
        if 1digit == 8 and 2digit == 9:
            print("{:d}{:d}".format(1digit, 2digit))
        else:
            print("{:d}{:d}".format(1digit, 2digit), end=", ")
