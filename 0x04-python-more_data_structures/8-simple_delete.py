#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """Deletes the provided key/value from a dictionary

       Args:
        @a_dictionary: python dictionary
        @key: string argument

       Return:
        A new dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
