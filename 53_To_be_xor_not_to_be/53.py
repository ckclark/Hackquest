msg = [
    '00000000',
    '00000000',
    '00000000',
    '00000000',
    '00011110',
    '00000100',
    '00000100',
    '00011011',
    '00000110',
    '01010100',
    '01000011',
    '00001001',
    '00001101',
    '00001001',
    '00010010',
    '00000001',
    '00010011',
    '00001001',
    '01000101',
    '01001001',
    '00011010',
    '01010011',
    '01001110',
    '01001000',
    '00001111',
    '00011010',
    '01001111',
    '01100001',
    '01101100',
]
s = ''.join(msg)
width = 8
cipher = []
for i in range(len(s) / width):
    cipher.append(int(s[i * width: (i + 1) * width], 2))

print cipher
key = 'The magic codeword is this!'
ans = []
for i in range(len(cipher)):
    k = key[i] if i < len(key) else '\x00'
    ans.append(chr(ord(k) ^ cipher[i]))
print ''.join(ans)

