#!/usr/bin/python3
"""
add arguments to a python list
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
open("add_item.json", "a")
try:
    l = load_from_json_file("add_item.json")
except ValueError:
    l = []
save_to_json_file(l + sys.argv[1:], "add_item.json")
