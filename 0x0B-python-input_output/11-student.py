#!/usr/bin/python3
"""
class that define student
"""


class Student:
    """c
    lass that define student
    """
    def __init__(self, first_name="Unknown", last_name="Unknown", age="0"):
        """
        initialisation mehode
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        dictionary representation
        """
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for i in attrs:
            try:
                dictionary[i] = self.__dict__[i]
            except:
                pass
        return dictionary

    def reload_from_json(self, json):
        """
        serialization and deserialization
        """
        for key, value in json.items():
            self.__dict__[key] = value
