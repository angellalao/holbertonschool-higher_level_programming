#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) != int:
        if type(a) == float:
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if type(b) != int:
        if type(b) == float:
            a = int(a)
        else:
            raise TypeError("b must be an integer")

    return (a + b)
