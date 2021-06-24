#!/usr/bin/python3

"""
function module
"""

if __name__ == '__main__':
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        arr = sys.argv[1]
    except Exception:
        arr = ""
    q = {"q": arr}
    x = requests.post(url, data=q)
    try:
        result = x.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exception:
        print("No result")
