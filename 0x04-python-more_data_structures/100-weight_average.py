#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple (<score>, <weight>)"""
    if my_list and len(my_list):
        num = 0
        dem = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            dem += tup[1]
        return (num / dem)
    return 0
