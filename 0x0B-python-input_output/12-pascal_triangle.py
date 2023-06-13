#!/usr/bin/python3
"""
A module solving the pascal's triangle
"""


def pascal_triangle(n):
    """
    Args:
        n: the nth item in the pascal's triangle
    Return:
        returns a list of lists of integers representing the Pascal's triangle
    """
    if n <= 0:  # return empty string if n is 0 or less
        return []

    pascal_tri = [[1]]  # initial triangle set to zero
    while (len(pascal_tri) != n):  # while we haven't reached n
        prev = pascal_tri[-1]  # initialize previous to the last row of matrix
        row = [1]  # initalize first item in the row

        for i in range(len(prev) - 1):  # sum each adjacent values, add list
            row.append(prev[i] + prev[i + 1])

        row.append(1)  # last item in the list
        pascal_tri.append(row)  # add the new row to matrix

    return (pascal_tri)
