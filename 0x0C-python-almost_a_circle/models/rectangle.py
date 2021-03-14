#!/usr/bin/python3
"""
rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init methode
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """
        getter
        """
        return self.__height

    @property
    def width(self):
        """
        getter
        """
        return self.__width

    @height.setter
    def height(self, height):
        """
        setter
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @width.setter
    def width(self, width):
        """
        setter
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    def display(self):
        """
        print reclangle with #
        """
        res = ""
        if self.__height == 0 or self.__width == 0:
            return res
        for i in range(self.__y):
            res += '\n'
        for row in range(self.__height):
            res += ' ' * self.__x + '#' * self.__width
            res += '\n'
        print(res[:len(res) - 1])

    @property
    def x(self):
        """
        getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        area
        """
        return self.__height * self.__width

    def __str__(self):
        """
        print instances
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self, *args, **kwargs):
        """
            update all attributes
        """
        if not len(args):
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        else:
            keys = ["id", "width", "height", "x", "y"]

            zipped_lists = zip(keys, args)
            zipped_lists = dict(zipped_lists)
            for key, val in zipped_lists.items():
                self.__setattr__(key, val)

    def to_dictionary(self):
        """
            return new dict
        """

        attrs = ["id", "width", "height", "x", "y"]
        return {key: getattr(self, key) for key in attrs}
