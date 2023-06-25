#!/usr/bin/python3
"""
script that adds arguments to a Python list,
and then save them to a JSON file
"""
import os
import sys
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


"""add obj to JSON file and then load from it"""
filename = "add_item.json"
if not os.path.exists(filename):
    my_list = []
else:
    my_list = load_from_json_file(filename)

new_item = sys.argv[1:]
for elem in new_item:
    my_list.append(elem)
save_to_json_file(my_list, filename)
