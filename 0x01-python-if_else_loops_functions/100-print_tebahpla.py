#!/usr/bin/python3
for num in range(122, 96, -1):
    print("{}".format(chr(num) if num % 2 == 0 else chr(num - 32)), end="")
