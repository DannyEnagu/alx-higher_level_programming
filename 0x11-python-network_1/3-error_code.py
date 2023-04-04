#!/usr/bin/python3
"""Takes in URL, sends a request to the URL and displays
   the body of the response using pythons urllib package.
   Also manages urllib.error.HTTPError exceptions.
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = Request(url)
        with urlopen(req) as response:
            print(response.read().decode())
    except HTTPError as e:
        print('Error code: ', e.code)
