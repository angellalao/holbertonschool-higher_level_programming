#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_tuple_a = list(tuple_a)
    list_tuple_b = list(tuple_b)

    if len(list_tuple_a) < 2:
        list_tuple_a = list_tuple_a + [0] * (2 - len(list_tuple_a))
    if len(list_tuple_b) < 2:
        list_tuple_b = list_tuple_b + [0] * (2 - len(list_tuple_b))

    new_a = list_tuple_a[0] + list_tuple_b[0]
    new_b = list_tuple_a[1] + list_tuple_b[1]
    new_tuple = (new_a, new_b)
    return new_tuple
