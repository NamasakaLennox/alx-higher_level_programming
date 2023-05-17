#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    prins a dictionary by ordered keys
    """
    sort = (sorted(a_dictionary.keys()))
    for elem in sort:
        print("{}: {}".format(elem, a_dictionary[elem]))
