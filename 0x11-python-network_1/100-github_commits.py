#!/usr/bin/python3
"""
function module
"""

if __name__ == '__main__':
    import sys
    import requests
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    repo_info = owner_name + "/" + repo_name
    url = "https://api.github.com/repos/" + repo_info + "/commits"
    x = requests.get(url)
    t = x.json()[:10]
    for w in t:
        h = w['sha']
        author = w['commit']['author']['name']
        print('{}: {}'.format(h, author))
