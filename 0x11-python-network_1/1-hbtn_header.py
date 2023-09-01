#!/usr/bin/python3
"""
takes a url, sends a request to the url and displays the values
of the X-Request-Id
"""
from sys import argv
from urllib import request

req = request.Request(argv[1])
with request.urlopen(req) as response:
    for key, value in response.headers.items():
        if key == 'X-Request-Id':
            print(value)
