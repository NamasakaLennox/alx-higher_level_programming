#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    adds only unique elements in the list
    """
    total = 0
    for elem in set(my_list):
        total += elem
    return (total)
