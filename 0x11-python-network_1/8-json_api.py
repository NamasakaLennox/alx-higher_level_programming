#!/usr/bin/python3
"""
requests from an api and searches for a letter
"""
if __name__ = '__main__':
    from sys import argv
    import requests

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': q}
    r = requests.post(url, data=params)

    try:
        res = r.json()
        if res:
            print('[{}] {}'.format(res['id'], res['name']))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
