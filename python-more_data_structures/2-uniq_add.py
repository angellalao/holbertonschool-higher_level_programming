#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = my_list.copy()
    for element in new_list:
        if new_list.count(element) > 1:
            new_list.remove(element)
    Sum = sum(new_list)
    return Sum
