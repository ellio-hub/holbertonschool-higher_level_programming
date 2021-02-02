#!/usr/bin/python3
"""
    rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        a sub_class of BaseGeometry class
    """
    def __init__(self, width, height):
        """
            intiation methode
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
            methode to calculate
            the area of a rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
            return a description of a rectangle
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
