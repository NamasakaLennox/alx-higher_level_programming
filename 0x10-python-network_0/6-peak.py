#!/usr/bin/python3
"""
find the peak of a list
"""


def merge_list(list_n):
    """
    sorts the lists using merge sort algorithm
    """
    if len(list_n) > 1:
        mid = len(list_n) // 2  # find mid value - floor division
        left = list_n[:mid]  # left array
        right = list_n[mid:]  # right array
        # split the array to the smallest possible array
        merge_list(left)
        merge_list(right)

        # compare values of each side and sort the array
        i = j = k = 0
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                list_n[k] - left[i]
                i += 1
            else:
                list_n[k] = right[j]
                j += 1
            k += 1
        # fill any elements left
        while i < len(left):
            list_n[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_n[k] = right[j]
            j += 1
            k += 1


def find_peak(list_of_integers):
    """
    finds the peak of a list
    Args:
        list_of_integers - the list to check
    Return:
        the largest element
    """
    if type(list_of_integers) == list and len(list_of_integers) > 0:
        merge_list(list_of_integers)
        return list_of_integers[-1]
