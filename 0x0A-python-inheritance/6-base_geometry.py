#!/usr/bin/python3
"""
contains a class with no area implementation
"""


class BaseGeometry:
    """
    The base class of a geometry class
    """
    def area(self):
        """
        raises an error exception when called
        """
        raise Exception("area() is not implemented")
