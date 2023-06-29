#!/usr/bin/python3
"""
This is a Python script that defines a base class named `Base`.

The `Base` class serves as a parent class for other classes in the codebase.
It includes a class attribute called `__nb_objects`, which keeps track of the
number of objects created from derived classes.
"""
import json


class Base:
    """
    Class: Base defined
    - Attributes:
        - __nb_objects: An integer representing the count of objects
          created from derived classes.
    - Methods:
        - __init__(self, id=None): The constructor method of the `Base` class.
          It initializes objects with a unique identifier.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an object of the Base class with a unique identifier.

        Parameters:
            id (int): Optional. An identifier for the object. Assigns the
                      given `id` to the `self.id` attribute.
                      If not provided, it generates a unique identifier for
                      the object based on the class attribute `__nb_objects`.

        Description:
            The `__init__` method is the constructor of the Base class.
            It is called when creating a new object, and assigns the object
            an id.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects = type(self).__nb_objects + 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string represenation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return f"[]"
        else:
            return json.dumps(list_dictionaries)
