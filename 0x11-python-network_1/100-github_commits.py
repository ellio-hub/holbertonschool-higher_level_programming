#!/usr/bin/python3
"""
function module
"""

if __name__ == '__main__':
    import sys
    import requests
    repo = sys.argv[1]
    owner = sys.argv[2]
    info = owner + "/" + repo 
    url = "https://api.github.com/repos/" + info + "/commits"
    x = requests.get(url)
    t = x.json()[:10]
    for w in t:
        h = w['sha']
        author = w['commit']['author']['repo']
        print('{}: {}'.format(h, author))

