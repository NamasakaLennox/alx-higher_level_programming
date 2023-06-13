#!/usr/bin/python3
"""
A module that contains a function that reads a given file
"""


def read_file(filename=""):
    """
    reads a given file passed as parameter
    Args:
        filename: the name of the file to be read
    prints the file contents int the stdout
    """
    with open(filename, encoding="utf-8") as file_open:
        text = file_open.read()
        print(text, end="")
