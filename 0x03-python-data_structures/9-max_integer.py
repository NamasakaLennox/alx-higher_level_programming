#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)

    if length == 0:
        return (None)
    maximum = my_list[0]
    for index in range(1, length):  # reassign maximum value for longer lists
        if my_list[index] > maximum:
            maximum = my_list[index]

    return (maximum)
