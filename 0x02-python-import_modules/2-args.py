#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:\n1: {}".format(argv[1]))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{}: {}".format(i + 1, argv[i + 1]))

if __name__ == "__main__":
    main()
