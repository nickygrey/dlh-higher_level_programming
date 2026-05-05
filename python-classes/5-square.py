#!/usr/bin/python3
"""Module for Square class."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Create a square."""
        self.size = size

    @property
    def size(self):
        """Return the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Change the size."""
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
