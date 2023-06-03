#!/usr/bin/python3
"""
A module containing a function `add_integer` that adds two integers
Adds only integers
casts floats to integers
"""


def add_integer(a, b=98):
    """
    function requires only one paramenter with an optional second
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    # cast a and b into integers
    a = int(a)
    b = int(b)
    return (a + b)
