#!/usr/bin/python3
"""
    Declares a new module: "LockedClass"
"""


class LockedClass:
    """Object Delaration "LockClass"

       LockClass prevents users from dynamically creating new
        instance attributes not specified in it's __slot__ list.
    """
    __slots__ = ["first_name"]
