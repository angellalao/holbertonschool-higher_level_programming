#!/usr/bin/python3

"""
module with definition of MyList class
"""


class MyList(list):
    """
    print_sorted(self): method that prints and sorts list
    """
    def print_sorted(self):
        """
        sorts and prints given list
        """
        sorted_list = sorted(self)
        print(sorted_list)
