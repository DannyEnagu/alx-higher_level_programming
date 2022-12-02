#!/usr/bin/python3


def element_at(my_list, idx):
    """Retive element from a list
       Args:
        idx: index of the element to retrive

       Return:
        The element in the index of idx or None if failed
    """
    if idx < 0:
        return (None)
    elif idx > (len(my_list) - 1):
        return (None)

    return (my_list[idx])
