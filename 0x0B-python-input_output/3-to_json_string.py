#!/usr/bin/python3
"""Defines the module ``3-to_json_string`` that defines
   the function ``to_json_string(my_obj)``
"""
import json


def to_json_string(my_obj):
    """Serialized a python object to a JSON string.

       Args:
        my_obj: A valid pyhton object

       Return:
        The JSON representation of an object (string)
    """
    return (json.dumps(my_obj))
