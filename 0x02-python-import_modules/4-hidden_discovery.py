#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    array = dir(hidden_4)
    for element in array:
        if (element[:2] == "__"):
            continue
        print(element)
