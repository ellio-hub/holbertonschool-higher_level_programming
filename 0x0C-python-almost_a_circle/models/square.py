#!/usr/bin/python3
"""
square modules
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
        class square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            init method
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
        getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        print string
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    def update(self, *args, **kwargs):
        """
            update attributes
        """
        attrs = ["id", "size", "x", "y"]
        if not args:  # args is empty
            for key, val in kwargs.items():
                setattr(self, key, val)
        else:
            zipped_lists = zip(attrs, args)
            zipped_lists = dict(zipped_lists)
            for key, val in zipped_lists.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
            return new dict
        """
        attrs = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attrs}
