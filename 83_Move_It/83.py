import urllib2
from PIL import Image
from cStringIO import StringIO
from glob import glob
from os.path import basename, splitext
from subprocess import Popen, PIPE
import re

COOKIE = 'Force=TG9vaywgYSBwYXNzd29yZCFVM0JsYkd4R2IzSmpaUT09; POSTNUKESID=eed81538658fbe878eb548ca919682a7; phpbb2mysql_data=a%3A1%3A%7Bs%3A6%3A%22userid%22%3Bs%3A6%3A%22170514%22%3B%7D; phpbb2mysql_sid=4ddc2331f06e24d84c1666b356d05b3a; ChallUID=170514; ChallUNAME=ckclark; PHPSESSID=b496f87af95c6546d6fa775fcf1d6a8f'
REFERER = 'http://www.rankk.org'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
HOST = 'hackquest.com'

def fetch_web(path, body=None):
    req = urllib2.Request(path, body)
    if body:
        req.add_header('Content-type', 'application/x-www-form-urlencoded')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
    req.add_header('Accept-Language', 'en-US,en;q=0.8')
    req.add_header('Cache-Control', 'max-age=0')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Cookie', COOKIE)
    req.add_header('Host', HOST)
    req.add_header('Referer', REFERER)
    req.add_header('User-Agent', USER_AGENT)

    fp = urllib2.urlopen(req)
    result = fp.read()
    return result

def main():
    mapping = {}
    for chess in glob('chess/*.png'):
        name = splitext(basename(chess))[0]
        im = Image.open(chess)
        if name.endswith('_'):
            name = name[0].upper()
        mapping[tuple(map(lambda x:x%2, im.getdata()))] = name
    move = ''
    step = 0
    pat = re.compile(r'bestmove (\w\d\w\d) ponder (?:\w\d\w\d|none)')
    while True:
        result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/34875637/wopr.php?move=' + move)
        open('%d.png' % step, 'wb').write(result)
        im = Image.open(StringIO(result))
        width, height = 33, 33
        board = []
        for i in range(8):
            ans = []
            for j in range(8):
                cell = im.crop((j * width, i * height, (j + 1) * width, (i + 1) * height))
                ans.append(mapping.get(tuple(map(lambda x:x % 2, cell.getdata())), ' '))

            ans = ''.join(ans)
            for i in range(8, 0, -1):
                ans = ans.replace(' ' * i, str(i))
            board.append(ans)
        board = '/'.join(board)
        input = []
        input.append('position fen ' + board + ' w kq - 0 1\n')
        input.append('setoption name Hash value 1024\n')
        input.append('go depth 15\n\n')
        input = ''.join(input)
        p = Popen(['./stockfish'], shell=False, stdin=PIPE, stdout=PIPE)
        result = p.communicate(input)[0]
        mat = pat.search(result)
        open('result', 'w').write(result)
        move = mat.group(1)
        move = [8 - int(move[1]), ord(move[0]) - ord('a'), 8 - int(move[3]), ord(move[2]) - ord('a')]
        print ''.join(map(str, move))
        move = str(int(''.join(map(str, move)), 8))
        step += 1

if __name__ == '__main__':
    main()
