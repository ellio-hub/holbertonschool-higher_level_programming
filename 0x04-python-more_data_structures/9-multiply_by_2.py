#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for x in new_dict.keys():
        new_dict[x] = a_dictionary[x] * 2
    return new_dict
