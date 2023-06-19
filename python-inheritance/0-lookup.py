#!/usr/bin/python3

"""
Module contains function that returns attributes and methods
of an  object
"""


def lookup(obj):
    """
    Returns list of available attributes and methods of object(obj)
    """
    return dir(obj)
