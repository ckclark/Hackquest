s = '00530065006300720065007400200070006100730073003a0020004200610074006d0061006e'
ans = []
for i in range(len(s) / 4):
    ans.append(chr(int(s[i * 4:i * 4 + 4], 16)))

print ''.join(ans)
