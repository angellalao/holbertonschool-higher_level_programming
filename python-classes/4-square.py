#!/usr/bin/python3

"""
Define a class square, with the private attribute size: Getter, setter,
and a public method.
"""


class Square:
    """
    Declare class Square

    Attributes:
       __size(int): Size of the square

    Methods:
       __init__(self, size=0): Initialises a new square instance
       area(self): Returns area of the square
    """

    def __init__(self, size=0):
        """
        Initialises a new square instance.

        Args:
           size(int): Size of the square. Default = 0.

        Raises:
           TypeError: If size is not an integer.
           ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
           int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
           value (int): Size of the square.

        Raises:
           TypeError: If value is not an integer.
           ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns area of the square

        Returns:
           int: Area of the square.
        """
        return self.__size ** 2
