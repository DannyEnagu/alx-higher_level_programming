#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
   using pythons urllib package.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    params = {}
    params['email'] = sys.argv[2]
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')  # data should be bytes
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(f"Your email is: {data.decode()}")
