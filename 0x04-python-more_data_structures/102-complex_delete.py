#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys in list(a_dictionary.keys()):
        if a_dictionary[keys] == value:
            del a_dictionary[keys]
    return (a_dictionary)
