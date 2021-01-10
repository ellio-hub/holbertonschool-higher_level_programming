#!/usr/bin/python3


def raise_exception_msg(message=""):
    try:
        a / 2
    except NameError:
        print(message)
