#!/usr/bin/python3
"""Defines the ``1-write_file`` module which contains
    the write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns
        the number of characters written

       Args:
        filename: path to file to write to.
        text: string data being written.

       Return:
        number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        data = f.write(str(text))
        return (data)
