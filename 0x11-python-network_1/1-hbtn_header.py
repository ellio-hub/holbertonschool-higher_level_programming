  #!/usr/bin/python3
"""
function module
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.getheader('X-Request-Id')

    print(content)
