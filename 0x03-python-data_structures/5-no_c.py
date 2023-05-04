#!/usr/bin/python3


def no_c(my_string):
    """Remove all characters c and C from a string

       Args:
        my_string: string input

       Return:
        A new string
    """
    new_str = ''
    i = 0

    for c in my_string:
        if c != 'c' and c != 'C':
            new_str = new_str + my_string[i]
        i += 1

    return (new_str)
