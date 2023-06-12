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

    def integer_validator(self, name, value):
        """
        validates an integer or value provided
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry class
    """
    def __init__(self, width, height):
        """
        a method that initialises object attributes
        Args:
            width: the width of rectangle
            height: the height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
