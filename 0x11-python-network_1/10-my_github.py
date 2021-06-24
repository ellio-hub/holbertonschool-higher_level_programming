#!/usr/bin/python3
"""
function module
"""

if __name__ == '__main__':
    import sys
    import requests
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    info = (username, password)
    x = requests.get(url, auth=info)
    try:
        print(x.json()['id'])
    except Exception:
        print('None')
