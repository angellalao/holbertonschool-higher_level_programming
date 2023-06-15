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
    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if type(b) != int:
        if type(b) == float:
            a = int(a)
        else:
            raise TypeError("b must be an integer")

    return (a + b)
