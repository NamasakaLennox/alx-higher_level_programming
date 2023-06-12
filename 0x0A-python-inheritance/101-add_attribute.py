#!/usr/bin/python3
"""
A module containing a function  that adds attributes to objects
"""


def add_attribute(obj, name, prop):
    """
    a function that adds new attributes to an object or class
    Args:
        obj: the object to add
        name: attribute name
        prop: the property of the attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, prop)
