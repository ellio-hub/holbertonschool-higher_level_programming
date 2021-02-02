#!/usr/bin/python3
"""
    main_module
"""


class MyInt(int):
    """
        sub_class of class int
    """
    def __init__(self, value):
        """
        initiation methode
        """
        self.value = value

    def __eq__(self, other):
        """
            method that define == operator
        """
        return self.value != other

    def __ne__(self, other):
        """
            method that define != operator
        """
        return self.value == other