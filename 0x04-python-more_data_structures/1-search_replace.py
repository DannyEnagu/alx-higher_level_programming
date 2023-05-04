#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrances of an element by
        another element in a new list

       Args:
        @my_list: is the initial list
        @search: is the element to replace in the list
        @replace: is the new element

       Return:
        A new list after replacement
    """
    res = []
    for i in range(0, len(my_list)):
        if my_list[i] == search:
            res.append(replace)
        else:
            res.append(my_list[i])

    return res
