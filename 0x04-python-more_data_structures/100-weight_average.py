#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    t = sum([x * y for x, y in my_list])
    q = t / sum([y for x, y in my_list])
    return q
