import urllib2
import urllib
import binascii
import re

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
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/1239845666/service.php')
    open('result.html', 'w').write(result)
    mat = re.search(r"Question: '(\w+)'", result)
    if mat:
        question = mat.group(1)
        crc = str(binascii.crc32(question) & 0xFFFFFFFF)
        print crc
        result2 = fetch_web('http://hackquest.com/modules/HackQuest/hacking/1239845666/service.php?answer=Checksum:' + crc)
        open('result2.html', 'w').write(result2)
        mat = re.match(r'The solution is: (\w+)', result2)
        print mat.group(1)
        if mat:
            result3 = fetch_web('http://hackquest.com/modules/HackQuest/hacking/1239845666/1239845666.php', urllib.urlencode({'solution':mat.group(1)}))
            open('pass.html', 'w').write(result3)

if __name__ == '__main__':
    main()
