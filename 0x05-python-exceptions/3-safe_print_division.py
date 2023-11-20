#!/usr/bin/python3

def safe_print_division(a, b):
    """
    divides a with b then returns the quotient
    """
    try:
        quotient = a / b
    except (TypeError, ZeroDivisionError):
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return (quotient)
