#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    prints elements that appear in only one of the lists
    """
    return (set(set_1 ^ set_2))
