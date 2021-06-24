#!/usr/bin/python3
"""
function module
"""

if __name__ == '__main__':
    import requests
    import sys
    para = {"email": sys.argv[2]}
    x = requests.post(sys.argv[1], data=para)
    print(x.text)
