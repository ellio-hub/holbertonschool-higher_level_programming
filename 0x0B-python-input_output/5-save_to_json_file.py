
#!/usr/bin/python3
"""
write Object to a text file with JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write Object to a text file with JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
