#!/usr/bin/python3

class Student:
    COHORT = "20"
    
    def __init__(self, name, age, card):
        self.name = name
        self.__age = age
        self.__card = card

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        print("In setter")
        self.__name = new_name.upper()

    @property
    def card(self):
        return self.__card[:4] + ("*" * (len(self.__card) - 4))
    
s = Student("Angella", 21, "1234567890")
s.name = "sophia"
print(s.card)
print(s.name)

s2 = Student("Kathryn", 21, "09873343343")
print(f"s.COHORT: {s.COHORT}")
#s.COHORT = "21"
#from pprint import pprint
#pprint(dir(s))
print(f"s2.COHORT: {s2.COHORT}")
print(f"Student.COHORT: {Student.COHORT}")
s.COHORT = "21"
print(f"s.COHORT: {s.COHORT}")
Student.COHORT = "22"
print(f"s.COHORT: {s.COHORT}")
print(f"s2.COHORT: {s2.COHORT}")
print(f"Student.COHORT: {Student.COHORT}")
