#!/usr/bin/python3
"""
A module with a function that prints the first and last name of a person
"""


def say_my_name(first_name, last_name=""):
    """
    takes two string parameters(one optional) and prints out the name
    """

    # check if arguments are strings
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
