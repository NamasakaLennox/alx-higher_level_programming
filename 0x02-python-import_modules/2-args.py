#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if (length == 1):
        print("{:d} argument:".format(length))
    else:
        print("{:d} arguments{}".format(length, ":" if length != 0 else "."))
    if (length > 0):
        for num in range(1, length + 1):
            print("{:d}: {}".format(num, argv[num]))
