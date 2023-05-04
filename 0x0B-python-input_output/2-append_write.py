#!/usr/bin/python3
"""Defines the module ``2-append_write`` and
   the function ``append_write(filename="", text="")``
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
        and returns the number of characters added

       Args:
        filename: path to file
        test: string data being added

       Return:
        The number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return (f.write(text))
