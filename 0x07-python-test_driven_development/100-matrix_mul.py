#!/usr/bin/python3
"""
A module that multiplies two matrices
Takes two arguments
"""


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices
    Args:
        m_a: first matrix
        m_b: second matrix
    Return:
        Returns the result of the multiplication
    """
    # check if argument is a list
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    # check if argument is a list of list
    for elem in m_a:
        if type(elem) != list:
            raise TypeError("m_a must be a list of lists")
    for elem in m_b:
        if type(elem) != list:
            raise TypeError("m_b must be a list of lists")
    # check if list is empty
    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    # each list should only be made up of integers or floats
    for elem in m_a:
        for items in elem:
            if type(items) != int and type(items) != float:
                raise TypeError("m_a should contain only integers or floats")
    for elem in m_b:
        for items in elem:
            if type(items) != int and type(items) != float:
                raise TypeError("m_b should contain only integers or floats")
    # ensure the matrix is rectangular
    size = len(m_a[0])
    for elem in m_a:
        if len(elem) != size:
            raise TypeError("each row of m_a must be of the same size")
    size = len(m_b[0])
    for elem in m_b:
        if len(elem) != size:
            raise TypeError("each row of m_b must be of the same size")

    # check if the two matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # the zip(*m_b) transposes the matrix m_b
    # the zip(row_a, col_b) pairs each row with corresponding column in a tuple
    result = list(list(sum(a * b for a, b in zip(row_a, col_b)) for col_b in
                       zip(*m_b)) for row_a in m_a)
    return (result)
