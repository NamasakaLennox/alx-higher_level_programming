#!/usr/bin/python3
"""
Module that prints a list in a sorted order
"""


class MyList(list):
    """
    Inherits a list object
    prints a list in a sorted order
    Args:
        list: the list object
    """


    def print_sorted(self):
        """
        prints the list in a sorted way
        """
        print(sorted(self))
