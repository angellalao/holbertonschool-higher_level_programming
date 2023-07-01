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
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string represenation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of list of instances to a file"""
        cls_name = f"{cls.__name__}.json"
        list_dict = []
        if list_objs is None:
            pass
        else:
            for list_obj in list_objs:
                list_dict.append(list_obj.to_dictionary())
        list_str = cls.to_json_string(list_dict)
        with open(cls_name, "w", encoding="utf-8") as f:
            f.write(list_str)

    @staticmethod
    def from_json_string(json_string):
        """convert json string to list. returnslist"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
