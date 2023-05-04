#!/usr/bin/python3
"""
   Defines ``5-base_geometry`` module which
    contains and a class ``BaseGeometry``
"""


class BaseGeometry:
    """Defines a new class ``BaseGeometry``."""

    def area(self):
        """Public intance method that raises an Exception
            with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
