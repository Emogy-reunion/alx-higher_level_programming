#!/usr/bin/python3
"""
adds all arguments to a Python list, and then saves them to a file
"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    list_json = load_from_json_file(filename)
except FileNotFoundError:
    list_json = []

for arg in argv[1:]:
    list_json.append(arg)

save_to_json_file(list_json, filename)
