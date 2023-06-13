#!/usr/bin/python3
"""
A module that converts a json file content into a python object
"""


import json


def load_from_json_file(filename):
    """
    reads a json file and converts contents into a python object
    Args:
        filename: name of the file to convert
    """
    with open(filename, encoding="utf-8") as file_open:
        text_obj = json.loads(file_open.read())
        return (text_obj)
