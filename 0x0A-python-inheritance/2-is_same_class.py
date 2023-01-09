#!/usr/bin/python3
"""
    Defines ``2-is_same_class`` module which contains
    one function ``is_same_class(obj, a_class)``.
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance
        of the specified class ; otherwise False

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return (True)
    False
