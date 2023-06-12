#!/usr/bin/python3
"""
contains a class with no area implementation
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns a formatted output string
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
