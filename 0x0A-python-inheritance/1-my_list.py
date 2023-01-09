#!/usr/bin/python3
"""
    Defines the "MyList" module.
"""


class MyList(list):
    """Defines a new class "MyList" that inherits from
        a list object.

        Args:
            list: list object.
    """

    def __init__(self):
        """Constructor function"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
