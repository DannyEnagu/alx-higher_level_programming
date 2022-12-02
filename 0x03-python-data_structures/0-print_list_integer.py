#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """Prints integers from a list
       Args:
        list: pyhton list of integer
       Return:
        Nothing
    """
    for i in my_list:
        print("{:d}".format(i))
