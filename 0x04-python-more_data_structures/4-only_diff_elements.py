#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """compare two sets and returns the difference

       Args:
        @set_1: first set
        @set_2: 2nd set

       Return:
        new set
    """
    return set_1 ^ set_2
