#!/usr/bin/python3

"""
Define a class rectangle
"""


class Rectangle:
    """
    A class representing a rectangle.

    Instance Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Class attributes:
        number_of_instances (int): Initialised to 0.
        print_symbol(any type): symbol used to print the rectangle.
    Methods:
        __init__(self, width=0, height=0): Initializes new rectangle instance.
        width(self): Getter method for retrieving the width of the rectangle.
        width(self, value): Method for setting the width of the rectangle.
        height(self): Getter method for retrieving the height of the rectangle.
        height(self, value): Method for setting the height of the rectangle.
        area(self): Method that returns area of rectangle.
        perimeter(self): Method that returns the perimeter of the rectangle.
        __str__(): Method that returns string representation of rectangle.
        __repr__(): Method taht returns string representation of rectangle.
        __del__(): Destructor.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle object with the specified width and height.
        Increments the class attribute number_of_instances (int) by 1.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Calculates and returns the area of the rectangle.

            Returns:
                int: The area of the rectangle.
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle object.

        Constructs a string representation of the rectangle. Using a sequence
        of characters(or any type) set by print_symbol class attribute, and
        a newline character is added after each row.

        Returns:
            str: The string representation of the rectangle object.
        """
        if self.height == 0 or self.width == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle = rectangle + str(self.print_symbol)
            if i != self.height - 1:
                rectangle = rectangle + "\n"
        return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle object
        that can be used to recreate the object.

        The returned string includes the class name and the values of
        width and height as arguments for recreating the rectangle object.

        Returns:
        str: The string representation of the rectangle object.

        """
        class_name = type(self).__name__
        return f"{class_name}({self.width}, {self.height})"

    def __del__(self):
        """
        Destructor method. Invoked when object is deleted.
        Prints string.
        Class attribute number_of_instances (int) is decremented by 1.
        """
        print(f"Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
