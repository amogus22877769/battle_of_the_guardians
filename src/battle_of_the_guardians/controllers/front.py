from os import environ

import requests

from src.battle_of_the_guardians.buffer import score


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

def set_score():
    with open('auth_data.txt') as f:
        s = f.read()
        username, password = s.split()
    f.close()
    r = requests.post('http://amogus22877769.heliohost.us/flasktest/score',
                      {'username': username, 'password': password, 'score': score[0]})
    return r.json()


class Front:
    pass