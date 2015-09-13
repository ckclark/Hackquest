# -*- coding:utf8 -*-
s = [
    '.,.,.,.',
    '......,',
    '..,..,,',
    '..,..,,',
    '..,.,,,',
    '...,,,,',
    '..,..,.',
    '....,..',
    ',...,.,',
    ',...,,.',
    '..,..,.',
    '...,..,',
    '....,..',
    '....,..',
    '...,,..',
    '....,.,',
    '...,,.,',
    '......,',
    '...,,,.',
]
ref = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZüöäÜÖÄ0123456789: '

s = ''.join(s)
ans = []
width = 7
for i in range(len(s) / width):
    line = s[i * width:(i + 1) * width]
    index = int(line.replace('.', '0').replace(',', '1'), 2)
    ans.append(ref[index - 1])

print ''.join(ans)

# riddleman
