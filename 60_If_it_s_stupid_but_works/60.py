s = '01101101011011110110111001101011011001010111100101110011'
ans = []
for i in range(len(s) / 8):
    ans.append(chr(int(s[i * 8:(i + 1) * 8], 2)))
print ''.join(ans)
