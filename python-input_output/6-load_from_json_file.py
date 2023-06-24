#!/usr/bin/python3
"""
This module defines a function  that reads a JSON file
and loads its contents into a Python object.
"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and loads its contents into a Python object.

    Parameters:
    - filename: The name of the JSON file to read.

    Returns:
    - A Python object representing the contents of the JSON file.

    The function opens the specified file in read mode ("r") and reads
    the entire contents using the `read()` method.
    The read contents are then passed to the `json.loads()` method,
    which parses the JSON string and returns a Python object.
    The function returns this Python object, representing the contents
    of the JSON file.

    If the file does not exist or is not a valid JSON file, an
    exception will be raised.
    """
    with open(filename, "r", encoding="utf-8") as f:
        chars_read = f.read()
        new_object = json.loads(chars_read)
        return new_object
