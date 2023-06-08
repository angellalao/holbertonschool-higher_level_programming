#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    dictlist = list(a_dictionary.values())
    dictlist.sort()
    max_val = dictlist[-1]
    for key, value in a_dictionary.items():
        if value == max_val:
            return key
