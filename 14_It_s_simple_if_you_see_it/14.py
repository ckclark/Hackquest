import urllib, urllib2
from lxml import etree

cookie = 'POSTNUKESID=3e1a7144cc3c02a1312a9f0b13b974c7; ChallUID=170514; ChallUNAME=ckclark'
referer = 'http://www.rankk.org'
body = None
post = None
parser = etree.HTMLParser()
solved = 0

path = 'http://www.hackquest.com/modules/HackQuest/hacking/253/253.php'
req = urllib2.Request(path, body)
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
req.add_header('Accept-Language', 'en-US,en;q=0.8')
req.add_header('Cache-Control', 'max-age=0')
req.add_header('Connection', 'keep-alive')
req.add_header('Cookie', cookie)
req.add_header('Host', 'www.hackquest.com')
req.add_header('Referer', referer)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1')
fp = urllib2.urlopen(req)
result = fp.read()

open('14.html', 'w').write(result)
