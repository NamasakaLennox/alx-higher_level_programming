#!/usr/bin/python3
"""
A module containing a function that converts a json string to a python object
"""


import json


def from_json_string(my_str):
    """
    converts a json string to an object
    Args:
        my_str: the json string
    returns the converted object
    """
    return (json.loads(my_str))
