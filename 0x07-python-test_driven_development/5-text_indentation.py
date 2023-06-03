#!/usr/bin/python3
"""
This module contains a function that prints a text with two new lines after
each character in `.?:`
"""


def text_indentation(text):
    """
    this function prints a string in a specified format
    Args:
        text: the string to be printed
    Return:
        Has no return value
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    string = ""
    i = 0
    length = len(text)
    while i < length:
        if i == 0:  # ensure it doesn't begin with a white space
            try:
                while text[i] == ' ':
                    i += 1
            except Exception:
                break
        string += text[i]

        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            string += "\n\n"
            i += 1
            try:
                while text[i] == ' ':
                    i += 1
            except Exception:
                break
        else:
            i += 1

    i = 0
    length = len(string) - 1
    # trim white spaces at the end
    if length != -1:
        while string[length] == " ":
            length -= 1
            i += 1
    if i != 0:
        string = string[:-i]
    print(string, end="")
