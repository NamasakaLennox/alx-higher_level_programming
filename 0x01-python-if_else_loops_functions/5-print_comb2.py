#!/usr/bin/python3
for num in range(100):
    if num < 10:
        string = "0" + str(num)
    else:
        string = num
    if num != 99:
        print("{}".format(string), end=", ")
    else:
        print("{}".format(string), end="\n")
