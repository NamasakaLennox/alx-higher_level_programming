#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    prints the first x elements in a list and only integers
    """
    items = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            items += 1
    print()
    return (items)
