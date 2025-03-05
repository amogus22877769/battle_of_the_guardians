from os import environ

import requests


def registration():
        code: int = 500
        r = {}
        with open('auth_data.txt') as f:
            s = f.read()
            username, password = s.split()
        f.close()
        while code != 200:
            r = requests.post('http://amogus22877769.heliohost.us/flasktest/authorization',
                          {'username': username, 'password': password})
            code = r.status_code
        print(r.json())
        return r.json()


class Front:
    pass