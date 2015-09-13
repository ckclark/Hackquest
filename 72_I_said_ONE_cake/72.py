import sys
from urllib import urlencode
sys.path.append('..')
from fetch_web import fetch_web

def main():
    data = urlencode({'name':'a' * 16, 'password':'p' * 16})
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/3/3.php', data)
    open('result.html', 'w').write(result)

if __name__ == '__main__':
    main()
