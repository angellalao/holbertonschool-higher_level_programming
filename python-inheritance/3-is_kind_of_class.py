#!/usr/bin/python3

"""
Module with function that checks if object is an
instance of the given class, or an instance of
one of its subclasses
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj  is an instance of a_class,
    or a subclass of a_class
    Returns True if yes, otherwise returns False
    """
    return isinstance(obj, a_class)
