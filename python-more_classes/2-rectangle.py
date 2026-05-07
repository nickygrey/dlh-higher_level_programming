#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Create a rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Change the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Return the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Change the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height * 2)
