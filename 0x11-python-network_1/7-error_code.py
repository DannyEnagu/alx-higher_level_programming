#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
   and displays the body of the response
"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)
