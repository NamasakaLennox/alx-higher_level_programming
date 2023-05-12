#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2, b1, b2 = 0, 0, 0, 0

    len1 = len(tuple_a)
    len2 = len(tuple_b)
    # unpack first tuple
    if len1 >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    elif len1 == 1:
        a1 = tuple_a[0]
    # unpack second tuple
    if len2 >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    elif len2 == 1:
        b1 = tuple_b[0]

    new_tuple = a1 + b1, a2 + b2
    return (new_tuple)
