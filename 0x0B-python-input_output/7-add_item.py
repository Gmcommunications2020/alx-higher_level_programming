#!/usr/bin/python3
"""Module 7"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    lista = load_from_json_file("add_item.json")
except FileNotFoundError:
    lista = []
for i in range(1, len(sys.argv)):
    lista.append(sys.argv[i])
save_to_json_file(lista, "add_item.json")
