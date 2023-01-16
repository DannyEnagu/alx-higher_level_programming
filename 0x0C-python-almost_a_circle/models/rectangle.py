#!/usr/bin/python3
"""Defines ``rectangle`` module that
    contains the ``Rectangle`` class.
"""
from models.base import Base


class Rectangle(Base):
    """Defines a new class ``Rectangle`` that inherits
        from ``Base`` class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new ``Rectangle`` class.
        Args:
            width:(int) ``Rectangle`` width.
            height:(int) ``Rectangle`` height.
            x:(int) x coordinate of ``Rectangle``.
            y:(int) y coordinate of ``Rectangle``.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the ``Rectangle`` instance with the character ``#``"""
        for h in range(self.height):
            [print("#", end="") for w in range(self.width)]
            print("")
