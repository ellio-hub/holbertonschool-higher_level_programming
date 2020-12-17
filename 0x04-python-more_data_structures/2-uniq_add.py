#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    s = 0
    for i in my_list:
        if i not in new_list:
            s += i
            new_list.append(i)
    return s
