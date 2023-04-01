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
    if lent == 2:
        return max(list_of_integers)

    mid = int(lent / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid + 1] and peak > list_of_integers[mid - 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
