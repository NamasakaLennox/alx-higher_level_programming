#!/usr/bin/python3
"""
A module with the function ``print_square`` that prints a square using "#"
Accepts integer values
"""


def print_square(size):
    """
    this function prints a square using the character "#"
    Args:
        size: the size of the square
    Return:
        No return value
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
