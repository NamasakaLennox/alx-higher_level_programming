#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes key in a dictionary
    """
    if key not in a_dictionary:
        return (a_dictionary)
    del a_dictionary[key]
    return (a_dictionary)
