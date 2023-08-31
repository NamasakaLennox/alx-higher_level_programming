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
    elif length == 1:
        return list_of_integers[0]
    elif length == 2:
        return (list_of_integers[0] if list_of_integers[0] >=
                list_of_integers[1] else list_of_integers[1])

    # for lists greater than 2 elements
    for i in range(length):
        # check if second element is smaller than first element
        if (i == 0 and list_of_integers[i + 1] <= list_of_integers[i]):
            return list_of_integers[i]
        # check if the items on the right and left of an element are both
        # less than the current integer
        elif (i > 0 and i < length - 1 and list_of_integers[i] >=
              list_of_integers[i + 1] and list_of_integers[i] >=
              list_of_integers[i - 1]):
            return (list_of_integers[i])
        # if the last item is larger than the previous item
        elif (i == length - 1 and list_of_integers[i - 1] <= value):
            return list_of_integers[i]
