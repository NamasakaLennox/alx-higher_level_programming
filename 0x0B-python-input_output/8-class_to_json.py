#!/usr/bin/python3
"""
A module that returns dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Returns dictionary description with simple data structure
    Args:
        obj: an instance of a class
    Return:
        the dictionary description
    """
    dictionary = {}
    if hasattr(obj, "__dict__"):
        dictionary = obj.__dict__.copy()
    return dictionary
