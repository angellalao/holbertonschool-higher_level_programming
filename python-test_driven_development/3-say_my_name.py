#!/usr/bin/python3

"""
 Contains function that prints string with first and last names as inputs
"""


def say_my_name(first_name, last_name=""):
    """
    Print a string  with the given first and last names.

    Arguments:
    - first_name: A string representing the first name.
    - last_name: (Optional) String representing last name. Default is empty.

    Returns:
    - None

    Raises:
    - TypeError: If the first_name or last_name is not a string.
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
