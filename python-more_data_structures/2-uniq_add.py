#!/usr/bin/python3

def uniq_add(my_list=[]):
    for element in my_list:
        if my_list.count(element) > 1:
            my_list.remove(element)
    Sum = sum(my_list)
    return Sum

