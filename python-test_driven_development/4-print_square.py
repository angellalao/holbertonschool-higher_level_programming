#!/usr/bin/python3

"""
Module contains function that prints square according to given size
"""


def print_square(size):
    """
    Prints square using "#" according to given size

    Arguments:
    - size: An integer representing the size of the square.

    Returns:
    - None

    Raises:
    - TypeError: If the size is not an integer.
    - ValueError: If the size is less than 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for i in range(size):
            print("#", end="")
        print()
