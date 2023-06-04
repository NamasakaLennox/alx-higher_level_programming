#!/usr/bin/python3
"""
A module that uses numpy to multiply a matrix
Takes two matrices as parameters
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the value
    Args:
        m_a: first matrix, a list of lists
        m_b: second matrix, list of lists
    Return:
        Product of the matrices
    """
    result = np.matmul(m_a, m_b)

    return (result)
