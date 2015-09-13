def decrypt(s):
    ans = []
    for i, c in enumerate(s):
        ans.append(chr(ord(c) - i))
    return ''.join(ans)

print decrypt('ppy1tmv')
