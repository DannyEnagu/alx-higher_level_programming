#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Multiple dictionary values and returns a new dictionary

       Args:
        @a_dictionary: python dictonary

       Return:
        A new dictonary
    """
    new_dict = []

    for i in list(a_dictionary):
        new_dict.append((i, a_dictionary[i]*2))
    return dict(new_dict)

