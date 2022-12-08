#!/usr/bin/python3
# Roman numerals and value in python integer
roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# Some special cases
sp_cases = [
    ("IV", '4'),
    ("IX", '9'),
    ("XL", '40'),
    ("XC", '90'),
    ("CM", '900')
]


def roman_to_int(roman_string):
    """ Converts Roman numeral to an integer

       Args:
        @roman_string: string input

       Return:
        Integer values on success, 0 if failed
    """
    rom_str = roman_string
    # Capitalize roman_srting
    rom_str = rom_str if rom_str.isupper() else rom_str.upper()

    # check if roman_string is not a string
    # or is equall to None
    if isinstance(rom_str, str) is not True or rom_str is None:
        return 0

    sum_t = 0

    # substitue all special characters in roman string
    for old, new in sp_cases:
        rom_str = rom_str.replace(old, new)

    # Add values to sum
    for i in list(rom_str):
        if i in roman_num:
            sum_t += roman_num[i]
        else:
            sum_t += int(i)

    return sum_t
