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

           Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value:

           Args:
               name: is always a string
               value: is an integer argument
           Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
