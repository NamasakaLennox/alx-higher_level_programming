#!/usr/bin/python3
"""
requests from an api and searches for a letter
"""

from sys import argv
import requests

if len(argv) > 1:
    val = argv[1]
else:
    val = ""

url = 'http://0.0.0.0:5000/search_user'
params = {'q': val}
r = requests.post(url, data=params)

try:
    res = r.json()
    if res:
        print('[{}] {}'.format(res['id'], res['name']))
    else:
        print('No result')
except requests.exceptions.JSONDecodeError:
    print('Not a valid JSON')
