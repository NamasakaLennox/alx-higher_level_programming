#!/usr/bin/python3
"""
A module that gets items in file and appends arguments provided to the program
Adds the contents to the file and saves the new contents
"""


import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = []

if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")

for items in sys.argv[1:]:
    my_list.append(items)

save_to_json_file(my_list, "add_item.json")
