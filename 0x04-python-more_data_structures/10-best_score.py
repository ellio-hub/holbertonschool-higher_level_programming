#!/usr/bin/python3

def best_score(a_dictionary):
    keyy = ""
    n = 0
    if a_dictionary:
        for k, i in a_dictionary.items():
            if i > n:
                keyy = k
                n = i
        return keyy
    else:
        return
