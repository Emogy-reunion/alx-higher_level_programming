#!/usr/bin/python3
""" print numbers 0 to 99"""
for numeral in range(0, 100):
    if numeral == 99:
        print("{}".format(numeral))
    else:
        print("{:02}".format(numeral), end=", ")
