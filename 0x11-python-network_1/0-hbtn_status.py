#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
   using pythons urllib package.
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status') as response:
        data = response.read()
        tab = '    '
        print(f"Body response:")
        print(f"{tab}- type: {type(data)}")
        print(f"{tab}- content: {data}")
        print(f"{tab}- utf8 content: {data.decode()}")
