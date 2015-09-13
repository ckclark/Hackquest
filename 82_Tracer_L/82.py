import urllib2
import glob
from os.path import basename
from PIL import Image

COOKIE = 'Force=TG9vaywgYSBwYXNzd29yZCFVM0JsYkd4R2IzSmpaUT09; POSTNUKESID=eed81538658fbe878eb548ca919682a7; phpbb2mysql_data=a%3A1%3A%7Bs%3A6%3A%22userid%22%3Bs%3A6%3A%22170514%22%3B%7D; phpbb2mysql_sid=56389b48e7a5e270194be2aafc26af30; ChallUID=170514; ChallUNAME=ckclark'
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
    xoffset = 5
    yoffset = 5
    width = 25
    height = 25
    mapping = {}
    for filename in glob.glob('alphabets/*.png'):
        im = Image.open(filename)
        c = basename(filename)[0]
        color = tuple(im.getdata())
        mapping[color] = c


    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/9841263762/service.php')
    open('alphabet.png', 'wb').write(result)
    im = Image.open('alphabet.png')
    pix = im.load()

    solution = []
    for i in range(4):
        color = []
        for y in range(height):
            for x in range(width):
                color.append(pix[x + xoffset + i * width, y + yoffset])
        solution.append(mapping[tuple(color)])

    for y in [41, 56]:
        offsetx = 8
        width = 5

        v = []
        for i in range(5):
            for j in range(4):
                x = i * 4 + j
                c = pix[offsetx + x * width, y]
                v.append(c)

        solution.append(mapping[tuple(v)])
    solution = ''.join(solution)
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/9841263762/service.php?answer=' + solution)
    open('result.html', 'w').write(result)


if __name__ == '__main__':
    main()
