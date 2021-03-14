#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    pascal triangle
    """
    if n <= 0:
        return []
    pascal = [[] for x in range(n)]
    pascal[0] = [1]
    if n > 1:
        pascal[1] = [1, 1]
    if n > 2:
        for i in range(2, n):
            pascal[i].append(1)
            for j in range(i - 1):
                pascal[i].append(pascal[i - 1][j] + pascal[i - 1][j + 1])
            pascal[i].append(1)
    return pascal
