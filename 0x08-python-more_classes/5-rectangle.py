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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
