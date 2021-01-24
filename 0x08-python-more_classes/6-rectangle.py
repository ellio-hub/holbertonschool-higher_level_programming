#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle Class"""
    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ public instance method
            to calculate the area of a rectangle
            Return:
                area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ public instance method
            to calculate the perimeter of a rectangle
            Return:
                perimeter
        """
        if self.area() == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """
        print a rectangle in STDOUT
        using the character #
        Returns:
            None
        """
        if self.area() == 0:
            return("")
        else:
            return(("#" * self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """string representation of a rectangle
            Return:
                string representation of a rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ methode to ensure proper
            deletion of the base class part
            of the instance
            and print a message to STDOUT
            args:
               none
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
