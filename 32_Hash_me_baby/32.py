
def hash(target):
    h = 0
    for i in range(len(target)):
        h += ord(target[i]) * i * i
    return h

def decode(target, phrase):
    while len(target) > len(phrase):
        phrase += phrase

    s1 = []
    for i in range(len(target)):
        s1.append(chr(ord(target[i]) - ord(phrase[i]) - i + 4))

    return ''.join(s1)

def hack(target, crypturl):
    ans = []
    for i in range(len(target)):
        ans.append(unichr(ord(crypturl[i]) - ord(target[i]) - i + 4))
    return ''.join(ans)


my_input = 'input'
urlchars = ['\261', '\320', '\323', '\327', '\336', '\324', '\352', '\232', '\343', '\333', '\311']
crypturl = ''.join(urlchars)

words = set(x.strip().lower() for x in open('/usr/share/dict/words').readlines() if x.strip().isalpha())
for w in words:
    if w.endswith('t') and len(w) == 7:
        s = decode(crypturl, w + '.php')
        if s.lower()[:-1] in words:
            print w + '.php', s.lower()[:-1]

