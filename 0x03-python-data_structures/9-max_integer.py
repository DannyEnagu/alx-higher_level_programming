#!/usr/bin/python3


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if len(my_list) == 0:
        return (None)

    max_t = 1
    for i in my_list:
        if i >= max_t:
            max_t = i

    return (max_t)
