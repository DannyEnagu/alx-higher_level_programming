#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
   using pythons urllib package.
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response.headers.get("X-Request-Id")
        print(data)
