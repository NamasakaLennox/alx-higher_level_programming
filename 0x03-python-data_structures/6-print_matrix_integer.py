#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elem in range(len(matrix)):  # iterate through each row
        elem_length = len(matrix[elem])  # length of each column

        for val in range(elem_length):  # iterate through each column
            num = matrix[elem][val]  # value contained in each row x column

            if (val == elem_length - 1):
                print("{:d}".format(num), end="")
            else:
                print("{:d}".format(num), end=" ")  # separate with space

            print()
