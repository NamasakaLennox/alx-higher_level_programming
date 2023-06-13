#!/usr/bin/python3
"""
A module with a function that appends text to a file
"""


def append_write(filename="", text=""):
    """
    A function that appends text to a file, creates new file if doesn't exist
    Args:
        filename: the name of the file
        text: the text to append
    """
    num_chars = 0
    with open(filename, "a", encoding="utf-8") as file_open:
        num_chars = file_open.write(text)
    return num_chars
