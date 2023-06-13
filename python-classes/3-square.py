#!/usr/bin/python3

"""
Create class square with optional instantiation: private attribute size.
Raises TypeError if size not int.
Raises ValueError if size < 0
Public instance method: area - returns square area
"""


class Square:
    """
    Defines class square

    Attributes: size(int)

    Methods:
    __init__(self, size=0): Initialises a new square instance
    area(self): Returns the area of the square
    """

    def __init__(self, size=0):
        """
        Initialises a new square insance.

        Args:
           size(int): The size of the square. Default = 0.

        Raises:
           TypeError: If size is not an integer
           ValueError: If size is < 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns the area of the square

        Returns:
           int: area of the square
        """
        return self.__size ** 2
