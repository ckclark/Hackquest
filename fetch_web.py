import urllib2

COOKIE = 'VIRUS!=Hello+I+am+a+virus%2C+and+I+come+from+HackQuest%21+Boooh%21+Be+scared%21; Force=TG9vaywgYSBwYXNzd29yZCFVM0JsYkd4R2IzSmpaUT09; POSTNUKESID=9f6e572df3133f95cb581adaf6da933b; phpbb2mysql_data=a%3A1%3A%7Bs%3A6%3A%22userid%22%3Bs%3A6%3A%22170514%22%3B%7D; phpbb2mysql_sid=e7edd74576e60627a5e00dee30951cd5; phpbb2mysql_t=a%3A3%3A%7Bi%3A1934%3Bi%3A1349795201%3Bi%3A2082%3Bi%3A1349795624%3Bi%3A240%3Bi%3A1349797114%3B%7D; PHPSESSID=f5444e114ac87272ae57a468bb4bc360; ChallUID=170514; ChallUNAME=ckclark'
REFERER = 'http://hackquest.com/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4'
HOST = 'hackquest.com'

def fetch_web(path, body=None, need_header=False, **kwargs):
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
    for k, v in kwargs.iteritems():
        req.add_header(k, v)

    fp = urllib2.urlopen(req)
    result = fp.read()
    if need_header:
        return result, fp.headers
    else:
        return result

def main():
    pass

if __name__ == '__main__':
    main()
