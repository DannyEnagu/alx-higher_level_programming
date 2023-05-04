#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
   using pythons urllib package.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    param = {}
    param["email"] = sys.argv[2]
    data = urllib.parse.urlencode(param).encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        data = response.read().decode()
        print(data)
