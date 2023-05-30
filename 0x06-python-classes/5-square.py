#!/usr/bin/python3
"""
A python module defining a class Square with private attributes
"""


class Square:
    """
    A class Square defining an attribute size
    """
    def __init__(self, size=0):
        """
        initializes an instance attribute with given value
        or zero if no value is given
        """
        self.size = size

    @property
    def size(self):
        """
        getter function to get the value of the private attribute
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setter function to set the value of private attribute
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        finds the area of a square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        a method that prints the square using the '#' character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
