#!/usr/bin/python3
"""
A python module defining a class Square with private attributes
"""


class Square:
    """
    A class Square defining an attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializes an instance attribute with given value
        or zero if no value is given
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        getter method for the position attribute
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        setter method for the position attribute
        """
        try:
            if type(value) != tuple:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if len(value) != 2:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if type(value[0]) != int or type(value[1]) != int:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            if x < 0 or y < 0:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
            else:
                self.__position = value

    def area(self):
        """
        finds the area of a square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        a method that prints the square using the '#' character
        """
        pos = self.__position
        if self.__size == 0:
            print()
        else:
            for i in range(pos[1]):
                print()
            for i in range(self.__size):
                for space in range(pos[0]):
                    print(end=" ")
                for j in range(self.__size):
                    print("#", end="")
                print()
