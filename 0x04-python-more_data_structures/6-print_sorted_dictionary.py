#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """Print a sorted dictionary both key and value
       Args:
        @a_dictionary: python dictionary

       Return:
        Nothing.
    """
    for i, j in sorted(a_dictionary.items()):
        print("{:s}: {}".format(i, j))
