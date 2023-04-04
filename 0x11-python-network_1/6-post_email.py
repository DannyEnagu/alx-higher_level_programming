#!/usr/bin/python3
"""Takes in a URL and an email address,
   sends a POST request to the passed URL
   with the email as a parameter, and finally
   displays the body of the response using
   pythons requests package.
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    param = {"email": sys.argv[2]}
    res = requests.post(url, param)
    print(res.text)
