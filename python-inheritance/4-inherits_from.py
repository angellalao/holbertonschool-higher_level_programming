#!/usr/bin/python3

"""
Module with function that checks if object is an instance
of a subclass of a specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of subclass of a_class,
    but not directly an instance of a_class
    """
    if isinstance(obj, a_class) is True:
        if type(obj) != a_class:
            return True
    return False
