#!/usr/bin/python3
"""
requests a url and displays values of a header file
"""
from sys import argv
import requests

if len(argv) > 1:
    r = requests.get(argv[1])
    print(r.headers.items())
