#!/usr/bin/python3
"""
returnn object represented by JSON
"""
import json


def from_json_string(my_str):
    """
    returnn object represented by JSON
    """
    return json.loads(my_str)
