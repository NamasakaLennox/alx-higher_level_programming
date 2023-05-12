#!/usr/bin/python3
def no_c(my_string):
    str_copy = ""
    for char in my_string:
        if (char == 'c' or char == 'C'):
            continue
        str_copy += char
    return (str_copy)
