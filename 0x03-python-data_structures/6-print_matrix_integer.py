#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in range(len(matrix)):  # iterate through each row
        for val in range(len(matrix[elem])):  # iterate through each column
            if (val != 0):
                print(end=" ")
            else:
                print("{:d}".format(matrix[elem][val]), end="")
        print()
