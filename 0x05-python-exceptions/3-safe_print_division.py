#!/usr/bin/python3


def safe_print_division(a, b):
    try:
        a = a / b
    except ZeroDivisionError:
        a = "none"
    finally:
        return(a)
