#!/usr/bin/python3
"""
This script defines a function to_json_string that converts an object
into its JSON representation.
"""
import json


def to_json_string(my_obj):
    """
    Converts an object into its JSON representation.

    Parameters:
    - my_obj: The object to be converted.

    Returns:
    - A JSON string representing the object.

    The function uses the json.dumps() method from the json module to
    convert the object into its JSON representation.
    The resulting JSON string is returned.
    """
    return json.dumps(my_obj)
