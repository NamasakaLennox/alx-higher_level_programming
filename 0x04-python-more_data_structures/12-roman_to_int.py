#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                  "M": 1000}
    temp_val = 0
    total = 0
    itr = 0
    sub = 0
    if type(roman_string) is not str or not roman_string:
        return (0)

    for i in range(len(roman_string)):
        if i + 1 < len(roman_string):
            if roman_dict[roman_string[i]] == roman_dict[roman_string[i + 1]]:
                temp_val += roman_dict[roman_string[i]]
                itr += 1
                if (itr != 3):
                    continue
            if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
                sub = roman_dict[roman_string[i]]
                continue

        total += temp_val + roman_dict[roman_string[i]] - sub
        temp_val = 0
        itr = 0
        sub = 0
    return (total)
