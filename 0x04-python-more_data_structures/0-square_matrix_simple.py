#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    returns the square of values in a 2d list
    """
    new_matrix = []
    for index in range(len(matrix)):
        new_matrix.append(list(map(lambda x: x ** 2, matrix[index])))
    return (new_matrix)
