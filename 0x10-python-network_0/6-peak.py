#!/usr/bin/python3
"""
function Module
"""


def div(array, b, t):
    """function to divide a list"""

    m = int((t + b)/2)
    if array[m-1] <= array[m] >= array[m+1]:
        return array[m]
    elif array[m] > array[m+1]:
        return div(array, b, m-1)
    elif array[m] < array[m+1]:
        return div(array, m+1, t)


def find_peak(arr):
    """Find peak"""

    if not arr:
        return None
    return div(arr, 0, len(arr)-1)
