#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Return rectangle with symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Return rectangle representation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @classmethod
    def square(cls, size=0):
        """Return new square rectangle."""
        return cls(size, size)

    def __del__(self):
        """Print delete message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
