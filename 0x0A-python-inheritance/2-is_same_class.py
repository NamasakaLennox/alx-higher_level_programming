#!/usr/bin/python3
"""
module containing a function
"""


def is_same_class(obj, a_class):
    """
    checks if an object is exactly an instance of a class
    """
    return type(obj) is a_class
