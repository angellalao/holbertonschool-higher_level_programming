#!/usr/bin/python3

""" Define class square with optional instantiation: size """


class Square:
    """
    Defines class Square
    
    Attributes:
       size (int): size of the square
    Methods:
       __init__(self, size=0): Initialises a new square instance
    """
    def __init__(self, size=0):
        """ 
        Initialises a new Square Instance
        
        Args:
        size (int): The size of the square. Default = 0
        
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
