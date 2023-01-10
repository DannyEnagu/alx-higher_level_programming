#!/usr/bin/python3
"""Defines a ``7-add_item`` module that contains a script
   that adds all arguments to a Python list, and then save
   them to a file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    # loads list object from text file.
    my_list = load_from_json_file(filename)

except FileNotFoundError:

    my_list = []

# add all items from command line arguments
# except item 1 to my_list.
my_list.extend(sys.argv[1:])

# save list object as text file
save_to_json_file(my_list, filename)
