#!/usr/bin/python3
"""
create Object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    create Object from JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
