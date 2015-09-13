import re
lines = open('68.txt').readlines()
pat = re.compile(r'\s+$')
ans = []
for line in lines:
    line = line.rstrip('\n')
    mat = pat.search(line)
    if mat:
        ans.append(chr(int(mat.group(0).replace(' ', '0').replace('\t', '1'), 2)))
print ''.join(ans)
