#!/usr/bin/python3
class LockedClass:
    """ conditional instance attribute creation
        Condition:
                attribute name = first_name
    """
    __slots__ = "first_name"