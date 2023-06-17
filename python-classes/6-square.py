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

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialises a new square instance.

        Args:
           size(int): Size of the square. Default = 0.
           position: position

        Raises:
           TypeError: If size is not an integer.
           ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Returns hidden position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set new position
        """
        error_msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(error_msg)
        if len(value) != 2:
            raise TypeError(error_msg)
        for num in value:
            if type(num) is not int:
                raise TypeError(error_msg)
            if num < 0:
                raise TypeError(error_msg)
        self.__position = value

    def area(self):
        """
        Returns area of the square

        Returns:
           int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using '#'.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                print()
