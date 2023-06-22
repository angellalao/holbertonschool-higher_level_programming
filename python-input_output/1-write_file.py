#!/usr/bin/python3

"""
module with function that writes a string into a
text file and returns the number of chars written
"""


def write_file(filename="", text=""):
    """
    writes string from "text" into text file
    (filename) and returns the number of chars written
    """
    with open(filename, "w+") as f:
        chars_written = f.write(text)
    return chars_written
