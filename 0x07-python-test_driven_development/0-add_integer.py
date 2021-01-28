#!/usr/bin/python3
"""add two number module
   returns the sum of its arguments.
   For numbers, that value is equivalent
   to using the ``+`` operator
"""


def add_integer(a, b=98):
    """function that cast numbers
        to integers and add them
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
