#!/usr/bin/python3
"""
module with function that writes an Object to a text file, using
a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Parameters:
    - my_obj: The object to be written to the file.
    - filename: The name of the file to write the object to.

    The function first converts the object into its JSON representation
    using the json.dumps() method.
    It then opens the specified file in write mode ("w+") and writes
    the JSON string to the file.
    The file is automatically closed when the "with" block is exited.

    Note: If the file already exists, its contents will be overwritten.

    The function does not return anything.
    """
    with open(filename, "w+", encoding="utf=8") as f:
        text = json.dumps(my_obj)
        chars_written = f.write(text)
