#!/usr/bin/python3
for first in range(10):
    for second in range(first, 10):
        if first == second:
            continue
        if first == 0 and second == 1:
            print("{}{}".format(first, second), end="")
        else:
            print(", {}{}".format(first, second), end="")
print()
