#!/usr/bin/python3
"""
Module that defines class square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class square that inherits from class rectangle defined """
    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints when print() or str() are invoked """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"

    @property
    def size(self):
        """retrieve size """
        return self.width

    @size.setter
    def size(self, value):
        """set width and height """
        self.width = value
        self.height = value
