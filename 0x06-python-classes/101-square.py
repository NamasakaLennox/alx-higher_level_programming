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
        self.size = size
        self.position = position

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
        if type(value) != tuple:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
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
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        a method that prints the square
        """
        string = ""
        if self.__size == 0:
            return (string)
        else:
            for i in range(self.__position[1]):
                string += "\n"
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    string += " "
                for j in range(self.__size):
                    string += "#"
                if i < self.__size - 1:
                    string += "\n"
        return (string)
