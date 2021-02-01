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
