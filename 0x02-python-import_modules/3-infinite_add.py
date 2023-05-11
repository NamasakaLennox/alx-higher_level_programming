#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    total_sum = 0
    if (length > 1):
        for num in range(1, length):
            total_sum += int(argv[num])
    print("{:d}".format(total_sum))
