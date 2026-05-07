#!/usr/bin/python3
"""Module that reads a text file and prints it."""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
