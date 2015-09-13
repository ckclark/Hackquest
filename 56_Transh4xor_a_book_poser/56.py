key = 'carnivore'
s = [
    'at te   euhesae 10 070elhfhrtti g s l 32108165teoi ootals.blt2430071a',
    'h rsio   yo e h400001c obm s ccr mawsi0300150 ua c hraebelain0210d0b ',
    'gsoinaanaitwrmg421c0f0 hifporc ltiaeps212060f  c htdkb cmy l.20131b0 ',
]
s = ''.join(s)
ans = []
for i in range(23):
    ans.append(s[i::23])
words = ''.join(ans).split()[:26]
# although the basic form of this cipher is not too hard to crack it can be a real ugly bitch sometimes. always beware all simple things. 32400422124032210013001121 00000c0308001d061717150f0b061c0b0f0e5a
first = '32400422124032210013001121'

ans = []
for i, word in enumerate(words):
    if first[i] != '0':
        ans.append(word[int(first[i]) - 1])
sol1 = ''.join(ans)

second = '00000c0308001d061717150f0b061c0b0f0e5a'

prev = 0
ans = []
for i in range(len(second) / 2):
    key = int(second[2 * i:2 * i + 2], 16)
    ans.append(chr(ord(sol1[i]) ^ key))
sol2 = ''.join(ans)
print sol1, sol2
