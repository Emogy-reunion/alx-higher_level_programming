#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divides elements from two lists one by one
    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: no of elements to divide
    Returns:
        a new list comtaining the quotients
    """
    div_list = []
    for k in range(0, list_length):
        try:
            quotient = my_list_1[k] / my_list_2[k]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            div_list.append(quotient)
    return (div_list)
