#!/usr/bin/python3

"""
Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
       a (int or float): First number.
       b (int or float): Second number. Default = 98.

    Returns:
       int: Sum of a and b.

    Raises:
       TypeError: If a or b is not an int or float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
