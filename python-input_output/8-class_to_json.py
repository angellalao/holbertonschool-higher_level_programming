#!/usr/bin/python3
"""
module contains function that returns a dictionary description
of an object, for json representation
"""


def class_to_json(obj):
    """
    returns attributes of an object in the form
    of a dictionary
    """
    dict_desc = vars(obj)
    return dict_desc
