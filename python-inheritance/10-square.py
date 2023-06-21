#!/usr/bin/python3
"""
Module that defines a Square class and inherits from the Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This class represents a Square and inherits from the Rectangle class.
    """
    def __init__(self, size):
        """
        Initializes a Square object.

        Parameters:
        - size (int): The size of the square's sides.

        Calls the superclass's __init__ method with the size argument for
        both width and height.
        Initializes private attribute __size with given size and validates it
        using the superclass's integer_validator method
        """
        self.__size = size
        super().__init__(size, size)
        super().integer_validator("size", self.__size)

    def area(self):
        """Returns area of the square """
        return super().area()
