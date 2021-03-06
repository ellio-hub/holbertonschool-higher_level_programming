#!/usr/bin/python3
""" divide a matrix """


def matrix_divided(matrix, div):
    """
        function that divides all elements of a matrix

        RETURNS:
                new matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    x = []
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(s)
    for i in matrix:
        if type(i) is not list:
            raise TypeError(s)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        k = []
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(s)
            if div == float('inf'):
                w = round(0)
            else:
                w = round(j / div, 2)
            k.append(w)
        x.append(k)
    return x
