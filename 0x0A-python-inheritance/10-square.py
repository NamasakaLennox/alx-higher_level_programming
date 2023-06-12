#!/usr/bin/python3
"""
A module containing a class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that inherits properties from the Rectangle class
    """
    def __init__(self, size):
        """
        Initializes the square class with its properties
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        gets the area of the square
        """
        return super().area()
