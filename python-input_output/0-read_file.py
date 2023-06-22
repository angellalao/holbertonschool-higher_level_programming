#!/usr/bin/python3

"""
module contains function that reads a text file and prints
it to the stdout
"""


def read_file(filename=""):
    """
    reads inputted file, and prints it to the standard output
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
