def decrypt(s):
    ans = []
    for c in s:
        ans.append(chr(ord(c) - 1))
    return ''.join(ans)

print decrypt('ejeju/qiq')
