#!/usr/bin/python3
def uppercase(str):
    for char in str:
        check = ord(char)
        if (check > 96 and check < 123):
            check -= 32
        print("{}".format(chr(check)), end="")
    print()
