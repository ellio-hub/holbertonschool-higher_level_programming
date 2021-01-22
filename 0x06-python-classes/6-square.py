#!/usr/bin/python3
""" square module """


class Square:
    """ square class """
    def __init__(self, size=0, position=(0, 0)):
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
        p = position
        if type(p) != tuple or (len(p) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(p[0]) != int or type(p[1]) != int or (p[0] * p[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.position[0], "#" * self.__size)

    @property
    def position(self):
        """
        postion getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            position setter
        Args:
            value (tuple): position of the square in the screen
        """
        if type(value) != tuple or len(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        p = value
        if type(p[0]) != int or type(p[1]) != int or (p[0] * p[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
