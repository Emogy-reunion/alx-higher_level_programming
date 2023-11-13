#!/usr/bin/python3
"""Print the numbers from 1 to 100 separated by a space."""


def fizzbuzz():
    for numeral in range(1, 101):
        if numeral % 3 == 0 and numeral % 5 == 0:
            print("FizzBuzz ", end="")
        elif numeral % 3 == 0:
            print("Fizz ", end="")
        elif numeral % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numeral), end="")
