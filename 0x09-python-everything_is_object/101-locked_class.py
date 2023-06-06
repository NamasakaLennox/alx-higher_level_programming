#!/usr/bin/python3
"""
Module containing a class that prevents user from dynamically creating
a new instance attribute of a class
"""


class LockedClass:
    """
    A class that prevents dynamic creation of instance attributes
    """
    __slots__ = ['first_name']

    def __init__(self, value=""):
        """
        initializes the first name variable with an optional value
        """
        self.first_name = value
