#!/usr/bin/python3
"""
Module description
"""
from models.base import Base


class Rectangle(Base):
    """defines class Rectangle, which inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiate class """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of rectangle"""
        return self.width * self.height

    def display(self):
        """print rectangle using #, with x,y as co-ordinates of where
           to print"""
        for blank_line in range(self.y):
            print("")
        for i in range(self.height):
            for blank_space in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """prints when print() or str() are invoked """
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.x}/{self.y}\
 - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns argument to attribute. used to update attribute value"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.width = kwargs["width"]
            except KeyError:
                pass
            try:
                self.height = kwargs["height"]
            except KeyError:
                pass
            try:
                self.x = kwargs["x"]
            except KeyError:
                pass
            try:
                self.y = kwargs["y"]
            except KeyError:
                pass

    def to_dictionary(self):
        """return dictionary representation of instance attributes"""
        keys = ["id", "width", "height", "x", "y"]
        new_dict = {}
        for i in keys:
            new_dict[i] = getattr(self, i)
        return new_dict
