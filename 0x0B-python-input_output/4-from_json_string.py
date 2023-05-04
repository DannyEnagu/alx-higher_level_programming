#!/usr/bin/python3
"""Defines the module ``4-from_json_string`` that defines
   the function ``4-from_json_string(my_str)``
"""
import json


def from_json_string(my_str):
    """Deserialized a JSON string to object (Python data structure).
       Args:
        my_str: A valid JSON strin
       Return:
        An object (Python data structure) represented by a JSON string
    """
    return (json.loads(my_str))
