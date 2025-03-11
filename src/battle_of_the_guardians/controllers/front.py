from time import time, sleep

import requests

from src.battle_of_the_guardians.buffer import score


def registration():
        code: int = 500
        r = {}
        time0 = time()
        with open('auth_data.txt') as f:
            s = f.read()
            username, password = s.split()
        f.close()
        while code != 200:
            if time() - time0 >= 3:
                return {'result': 'fail'}
            r = requests.post('http://amogus22877769.heliohost.us/flasktest/authorization',
                          {'username': username, 'password': password})
            code = r.status_code
        print(r.json())
        return r.json()

def set_score():
    code: int = 500
    r = {}
    time0 = time()
    with open('auth_data.txt') as f:
        s = f.read()
        username, password = s.split()
    f.close()
    while code != 200:
        if time() - time0 >= 3:
            return {'result': 'fail'}
        r = requests.post('http://amogus22877769.heliohost.us/flasktest/score',
                          {'username': username, 'password': password, 'score': score[0]})
        code = r.status_code
    print(score[0], r.status_code, r.content)
    return r.json()

def leaderboard():
    code: int = 500
    r = {}
    time0 = time()
    while code != 200:
        if time() - time0 >= 3:
            return {'result': 'fail'}
        r = requests.get('http://amogus22877769.heliohost.us/flasktest/leaderboard')
        code = r.status_code
    print(score[0], r.status_code, r.content)
    return r.json()