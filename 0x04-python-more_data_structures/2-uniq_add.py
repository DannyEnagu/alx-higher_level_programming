#!/usr/bin/python3


def uniq_add(my_list=[]):
    """Add all unique integers in a list

       Args:
        @my_list: initial list

       Return:
        sum of all unique integers
    """
    sum = 0

    for i in list(set(my_list)):
        sum += i

    return sum
