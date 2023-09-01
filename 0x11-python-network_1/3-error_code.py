#!/usr/bin/python3
"""
takes a url, sends a request and displays the body of the response
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if len(argv) > 1:
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
