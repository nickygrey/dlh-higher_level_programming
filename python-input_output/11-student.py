#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Create a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the object."""
        if type(attrs) is list:
            new_dict = {}

            for item in attrs:
                if item in self.__dict__:
                    new_dict[item] = self.__dict__[item]

            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """Replace student attributes from a dictionary."""
        for key in json:
            self.__dict__[key] = json[key]
