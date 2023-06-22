#!/usr/bin/python3

"""
module with function tha appends text to end of text file
"""


def append_write(filename="", text=""):
    """
    Appends text from 'text' argument to the
    end of text file ('filename' argument)
    Returns: number of chars added"""
    with open(filename, "a") as f:
        chars_written = f.write(text)
    return chars_written
