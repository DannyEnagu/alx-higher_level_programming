#!/usr/bin/python3
"""Defines a ``0-read_file`` module.
   And a ``read_file`` function.
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

       Args:
        filename: path to file being read.
    """
    with open(filename, encoding="utf-8") as f:
        data = f.read()
        print(data)
