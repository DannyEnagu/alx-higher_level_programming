#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
   displays the value of the variable X-Request-Id
   in the response header uses response package
"""


if __name__ == "__main__":
    import requests
    import sys
    res = requests.get(sys.argv[1])
    print(res.headers.get('X-Request-Id'))