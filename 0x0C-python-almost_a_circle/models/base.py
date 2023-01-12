#!/usr/bin/python3
"""Defines a module ``base`` that contains the
    ``Base`` class
"""


class Base:
    """Defines a new class ``Base``."""
    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes ``Base`` class constructor.

           Args:
            id(int): Argument to instance attribute.
        """
        # Public instance attribute
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
