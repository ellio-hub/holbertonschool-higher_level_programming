#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "DM": 900,
        "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400
    }
    i = 0
    if isinstance(roman_string, str):
        l = len(roman_string)
        c = 0
        while c < l:
            if c + 1 < l and roman_string[c:c + 2] in roman:
                i += roman[roman_string[c:c + 2]]
                c += 2
            else:
                i += roman[roman_string[c]]
                c += 1
    return i
