#!/usr/bin/python3
"""
sends a request and displays the body of the response
"""
from sys import argv
import requests

if len(argv) > 1:
    url = argv[1]
    r = requests.get(url)
    if (r.status_code >= 400):
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
