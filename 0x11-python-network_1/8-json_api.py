#!/usr/bin/python3
"""Takes in a letter and sends a POST request
   to http://0.0.0.0:5000/search_user with the
   letter as a parameter.
"""


if __name__ == "__main__":
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    q_char = ""
    if len(sys.argv) > 1:
        q_char = sys.argv[1]
    data = {"q": q_char}
    res = requests.post(url, data)
    try:
        res = res.json()
        if res:
            u_id = res.get("id")
            u_name = res.get("name")
            print(f"[{u_id}] {u_name}")
        else:
            print("No result")

    except Exception as e:
        print("Not a valid JSON")
