#!/usr/bin/python3
"""Defines the module ``5-save_to_json_file`` that defines
   the function ``save_to_json_file(my_obj, filename)``
"""
import json


def save_to_json_file(my_obj, filename):
    """Serializes an Object to a text file, using a
        JSON representation

       Args:
        my_obj: Any valid python objest
        filename: path to file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
