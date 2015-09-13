import sys
from hashlib import md5
sys.path.append('..')
from fetch_web import fetch_web

def main():
    result = fetch_web('http://hackquest.com/modules/HackQuest/hacking/9/challenge.php', Cookie='pass=' + md5('SickPuppy').hexdigest())
    open('result.html', 'w').write(result)
    # Get the password: copacabana, enter it in enterpassword.php

if __name__ == '__main__':
    main()
