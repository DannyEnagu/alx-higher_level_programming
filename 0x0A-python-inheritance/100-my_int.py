#!/usr/bin/python3
"""Defines a module ``100-my_Int``"""


class MyInt(int):
    """Defines a new class ``MyInt`` is a rebel as it
       Invert int operators == and !=.
    """

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
