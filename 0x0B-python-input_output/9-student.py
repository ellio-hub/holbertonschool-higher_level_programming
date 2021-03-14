#!/usr/bin/python3
"""
class that defines studen
"""


class Student():
    """
        class that defines studen
    """
    def __init__(self, first_name, last_name, age):
        """
            INIT
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            dictionary representation
        """
        return(self.__dict__)
