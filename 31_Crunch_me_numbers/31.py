def decrypt(target, phrase):
    while len(target) > len(phrase):
        phrase += phrase

    s1 = []
    for i in range(len(target)):
        s1.append(unichr(ord(target[i]) - ord(phrase[i]) - i))

    return ''.join(s1)

def encrypt(target, phrase):
    while len(target) > len(phrase):
        phrase += phrase


    s1 = []
    for i in range(len(target)):
        s1.append(unichr(ord(target[i]) + ord(phrase[i]) + i))

    return ''.join(s1)

def hack(crypturl, cryptpass):
    while len(crypturl) < len(cryptpass):
        crypturl += crypturl

    ans = []
    for i in range(len(cryptpass)):
        ans.append(unichr(ord(cryptpass[i]) - i - ord(crypturl[i])))
    return ''.join(ans)



urlchars = ['\301', '\317', '\310', '\332', '\227', '\351', '\271', '\334']
crypturl = ''.join(urlchars)

passchars = [u'\u0114',u'\u0135',u'\u012D',u'\u014F',u'\u0100',u'\u0162',u'\u010A',u'\u0148',u'\u0142']
cryptpass = ''.join(passchars)

my_input = hack(crypturl, cryptpass)

newpass = encrypt(my_input, crypturl)
crypturl = decrypt(crypturl, my_input)

if newpass == cryptpass:
    print crypturl

