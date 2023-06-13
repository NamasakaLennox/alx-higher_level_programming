#!/usr/bin/python3
"""
A module that writes an object into a file as a json string
"""


import json


def save_to_json_file(my_obj, filename):
    """
    A function that saves an object in a json file
    Args:
        my_obj: the object to write to file
        filename: the name of file to write
    """
    with open(filename, "w", encoding="utf-8") as file_open:
        file_open.write(json.dumps(my_obj))
