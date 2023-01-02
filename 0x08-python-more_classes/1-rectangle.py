#!/usr/bin/python3
"""
    Declares a new "rectangle" module.
    The rectangle module supplies one class, Rectangle.
"""


class Rectangle:
    """class Declaration "Rectangle"."""
    def __init__(self, width=0, height=0):
        """Initialize a new Regtangle instance

            Args:
             @width: integer input for Rectangle width
             @height: integer input for Rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of each Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of  each Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of each Retangle instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of each Rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value
