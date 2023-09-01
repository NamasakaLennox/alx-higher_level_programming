#!/usr/bin/python3
"""
prints the last 10 commits of a repository 'rails' by user 'rails'
"""
from sys import argv
import requests

if len(argv) > 2:
    user = argv[1]
    repo = argv[2]
    url = 'https://api.github.com/repos/' + user + '/' + repo + '/commits'
    r = requests.get(url)
    try:
        commits = r.json()
        for i in range(10):
            print('{}: {}'.format(commits[i]['sha'],
                                  commits[i]['commit']['author']['name']))
    except Exception:
        pass
