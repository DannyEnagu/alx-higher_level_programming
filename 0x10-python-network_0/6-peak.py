#!/usr/bin/python3
"""Contains the function ``find_peak`` """


def find_peak(list_of_integers):
    """Function that finds a peak in a list
       of unsorted integers.

       Argument:
       list_of_integers: list of integers.
    """
    if list_of_integers == []:
        return None

    lent = len(list_of_integers)

    if lent == 1:
        return list_of_integers[0]
    mid = int(lent / 2)
    peak_l = max(list_of_integers[:mid])
    peak_r = max(list_of_integers[mid:])

    if peak_l > peak_r:
        return peak_l
    elif peak_r > peak_l:
        return peak_r
    else:
        return peak_l
