#!/usr/bin/python3
"""
A module with a function that writes into a given file
"""


def write_file(filename="", text=""):
    """
    write_file:
        writes into a given file, creates a new file if it doesn't exits,
        overwrites old file if it exists
    Args:
        filename: the name of the file
        text: the text to be written
    """
    num_chars = 0
    with open(filename, "w", encoding="utf-8") as file_open:
        num_chars = file_open.write(text)
    return num_chars
