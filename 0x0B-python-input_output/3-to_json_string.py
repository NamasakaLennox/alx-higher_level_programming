#!/usr/bin/python3
"""
A module with a function that returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    Returns the json representation of an object
    Args:
        my_obj: the string to convert to JSON representation
    """
    return (json.dumps(my_obj))
