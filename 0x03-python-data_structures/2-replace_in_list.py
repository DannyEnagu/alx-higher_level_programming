#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replace element of a list at a given index

       Args:
        my_list: valide python list
        idx: index of list to replace
        element: new data to add to list

       Return:
        New list on success or old list if failed
    """
    if idx < 0:
        return (my_list)
    elif idx > (len(my_list) - 1):
        return (my_list)
    else:
        my_list[idx] = element

    return (my_list)
