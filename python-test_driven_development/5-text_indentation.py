#!/usr/bin/python3

"""
Module contians function that prints given body of text, with certain
indentations.
"""


def text_indentation(text):
    """
    Print the given text with 2 newlines after specific characters:
    (".", "?", ":")

    Arguments:
    - text: A string to be indented.

    Returns:
    - None

    Raises:
    - TypeError: If the text is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    character = [".", "?", ":"]
    prev_char = 0
    for letter in text:
        if letter == " " and prev_char == 1:
            continue
        prev_char = 0
        print(letter, end="")
        if letter in character:
            prev_char = 1
            print()
            print()
