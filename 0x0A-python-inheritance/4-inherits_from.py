#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is inherited (directly or indirectly) to a_class 
        - True. Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
