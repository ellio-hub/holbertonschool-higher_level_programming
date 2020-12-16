#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("0")
    elif len(argv) == 2:
        print("{}".format(argv[1]))
    elif len(argv) > 2:
        s = 0
        for i in range(len(argv) - 1):
            s = s + int(argv[i + 1])
        print("{}".format(s))

if __name__ == "__main__":
    main()
