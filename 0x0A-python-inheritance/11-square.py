#!/usr/bin/python3
"""
    square module
"""


rectangle = __import__('9-rectangle').Rectangle


class Square(rectangle):
    """
        classc square
    """
    def __init__(self, size):
        """
            intiation method
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
            methode to calculate
            the area of a rectangle
        """
        return self.__size ** 2

    def __str__(self):
        """
            return a description of a square
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
