#!/usr/bin/python3
"""
    1-my_list module
"""


class MyList(list):
    """
        sub-class of list class
    """

    def print_sorted(self):
        """
            prints given list,
            but sorted (ascending sort)
        """
        print(sorted(self))
