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

    def area(self):
        """
            square area
            Return:
                square area
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size getter
        Return:
            square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        Args:
            size (int): size of square
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        print a square in STDOUT
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for x in range(self.__size):
                    print("#", end="")
                print()
