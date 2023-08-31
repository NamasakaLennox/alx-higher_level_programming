#!/usr/bin/python3
"""
find the peak of a list
"""


def find_peak(list_of_integers):
    """
    finds the peak of a list
    Args:
        list_of_integers - the list to check
    Return:
        the largest element
    PS: merge sort takes O(log(n) so not worth sorting
    """

    if type(list_of_integers) != list:
        return
    length = len(list_of_integers)
    if length == 0:
        return

    peak = list_of_integers[0]
    i = 1
    length -= 1
    # for lists greater than 1 element
    while i <= length:
        # check from front
        if list_of_integers[i - 1] > list_of_integers[i]:
            return list_of_integers[i - 1]
        # check from back
        elif list_of_integers[length] > list_of_integers[length - 1]:
            return list_of_integers[length]
        else:
            peak = list_of_integers[i]
        i += 1
        length -= 1

    return peak
