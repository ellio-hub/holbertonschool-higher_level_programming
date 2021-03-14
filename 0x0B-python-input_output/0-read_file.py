#!/usr/bin/python3
"""
reads a text file and print to stdout
"""


def read_file(filename=""):
    """
    reads a text file and print to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
