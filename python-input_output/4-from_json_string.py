#!/usr/bin/python3
"""
contains function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    converts JSON encoded data into a Python object.
    returns a dictionary
    """
    return json.loads(my_str)
