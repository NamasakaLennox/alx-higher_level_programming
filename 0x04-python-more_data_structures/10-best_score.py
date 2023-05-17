#!/usr/bin/python3
def best_score(a_dictionary):
    """
    returns the highest score in a dictionary
    """
    if not a_dictionary:
        return (None)
    max_val = a_dictionary[list(a_dictionary.keys())[0]]
    for key in a_dictionary:
        if a_dictionary[key] > max_val:
            max_key = key
    return (max_key)
