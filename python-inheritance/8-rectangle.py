#!/usr/bin/python3

"""
class Rectangle created, which inherits from class BaseGeometry
"""
BaseGeometry = __import__(7-base_geometry).BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle = Subclass to BaseGeometry created.
    Arguments width and height are validated through
    integer_validator method inherited from parent class
    """
    def __init__(self, width, height):
        """
        Initialise subclass rectangle with width and height
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
