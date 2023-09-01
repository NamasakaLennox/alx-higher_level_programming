#!/usr/bin/python3
"""
takes a url and an email address and sends a post request
displays the body of the response
"""
from sys import argv
import requests

if len(argv) > 2:
    url = argv[1]
    email = argv[2]
    value = {'email': email}
    try:
        r = requests.post(url, value)
        print(r.text)
    except Exception:
        pass
