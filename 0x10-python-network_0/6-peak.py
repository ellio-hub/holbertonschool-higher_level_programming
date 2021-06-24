#!/usr/bin/python3
"""
function Module
"""


def find_peak(x):
    """Find peak"""

    if x == []:
        return None
    if len(x) == 1:
        return x[0]
    if x[0] >= x[1]:
        return x[0]
    if x[len(x) - 1] >= x[len(x) - 2]:
        return x[len(x) - 1]
    for i in range(1, len(x) - 1):
        if x[i] >= x[i - 1] and x[i] >= x[i + 1]:
            return x[i]
