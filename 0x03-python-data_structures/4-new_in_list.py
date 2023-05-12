#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    copy = my_list.copy()
    if (idx < 0 or idx >= length):
        return (copy)
    copy[idx] = element
    return (copy)
