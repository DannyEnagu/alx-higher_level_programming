#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a dictonary key with the biggest value"""

    if not a_dictionary:
        return None

    biggest_k = ''
    max_v = 0

    for i in list(a_dictionary):
        if max_v < a_dictionary[i]:
            max_v = a_dictionary[i]
            biggest_k = i

    return biggest_k
