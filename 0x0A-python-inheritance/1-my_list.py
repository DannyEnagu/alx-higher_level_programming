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
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""

        my_list = []

        for i in range(super().__len__()):
            my_list.append(super().__getitem__(i))

        my_list.sort()
        print(my_list) 
