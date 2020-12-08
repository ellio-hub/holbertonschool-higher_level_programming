#!/usr/bin/python3
def remove_char_at(str, n):
    c = ''
    if n < 0 or n >= len(str):
        return str
    for i in range(len(str)):
        if i != n:
            c += str[i]
    return c
