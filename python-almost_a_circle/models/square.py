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

    def update(self, *args, **kwargs):
        """assigns argument to attribute. update attribute value """
        attribute_list = ["id", "size", "x", "y"]
        for i in args:
            try:
                setattr(self, attribute_list[args.index(i)], i)
            except KeyError:
                pass
        for j in kwargs:
            try:
                setattr(self, j, kwargs[j])
            except KeyError:
                pass
