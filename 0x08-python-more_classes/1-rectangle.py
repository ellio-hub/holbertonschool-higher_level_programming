#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """initialization method
        args:
            width = width of a rectangle
            height = height of a rectange
        return:
            none
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter to retrieve width attribute
        Return:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter to set width attribute
        return:
            none
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter to retrieve height attribute
        Return:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter to set height attribute
        return:
            none
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
