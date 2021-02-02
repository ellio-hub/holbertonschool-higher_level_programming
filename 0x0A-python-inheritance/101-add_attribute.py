#!/usr/bin/python3
"""
    main_module
"""


def add_attribute(object, attribute, value):
    """
        function that adds a
        new attribute to an
        object if it’s possible
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
