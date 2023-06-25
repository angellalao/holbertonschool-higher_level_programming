#!/usr/bin/python3
"""
module that creates a class Student
"""


class Student:
    """class Student defined """
    def __init__(self, first_name, last_name, age):
        """
        instantiate instance with first_name, last_name and age attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dictionary representation of a Student instance"""
        return self.__dict__
