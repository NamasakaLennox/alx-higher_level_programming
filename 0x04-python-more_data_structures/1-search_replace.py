#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    searches for an element in a list and replaces it with the desired one
    """
    new_list = []
    for index in range(len(my_list)):
        if (my_list[index] == search):
            new_list.append(replace)
        else:
            new_list.append(my_list[index])
    return (new_list)
