#!/usr/bin/python3
""" square module """


class Square:
    """ square class """
    def __init__(self, size=0):
        """
        intilization methode
        Args:
            size (int): This defines the size of the square.
         """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
