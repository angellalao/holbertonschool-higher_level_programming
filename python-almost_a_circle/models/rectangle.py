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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.__x = value

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.__y - value
