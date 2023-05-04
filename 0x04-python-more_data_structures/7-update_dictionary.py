#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Replace or add a new key/value to a dictionary

       Args:
        @key: string argument
        @value: argument of any data type

       Return:
        A new dictionary
    """
    a_dictionary[key] = value

    return a_dictionary
