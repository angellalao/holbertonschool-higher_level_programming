#!/usr/bin/python3

"""
Module contains function that checks if object is
exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Check if given object is exactly an instance of a given
    class.
    Returns: True if yes, otherwise False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
