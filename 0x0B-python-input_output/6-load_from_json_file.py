#!/usr/bin/python3
"""Defines the ``6-load_from_json_file`` module which contains
    one ``loda_from_json_file`` function.
"""
import json


def load_from_json_file(filename):
    """load_from_json_file - Creates an Object from a “JSON file”.

       Args:
        filename: path to filei

       Return:
        The created object.
    """
    with open(filename, encoding="utf-8") as f:
        return (json.loads(f.read()))
