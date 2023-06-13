#!/usr/bin/python3
"""
A module that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Searches for a specific string and adds a line of text to file if string
    is present
    Args:
        filename: name of the file
        search_string: the string to search
        new_string: the string to insert
    """
    text = ""
    # open and search the file
    with open(filename, encoding="utf-8") as file_open:
        for line in file_open:
            text += line
            if search_string in line:
                text += new_string

    # open and write into the file
    with open(filename, "w", encoding="utf-8") as file_write:
        file_write.write(text)
