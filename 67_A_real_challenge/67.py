fp = open('square.bmp', 'rb')
fp.seek(54)
diff = []
b, g, r = (ord(fp.read(1)) for _ in range(3))
diff.append('1' if b != 0x60 else '0')
diff.append('1' if g != 0x91 else '0')
diff.append('1' if r != 0x3c else '0')

for i in range(48):
    b, g, r = (ord(fp.read(1)) for _ in range(3))
    diff.append('1' if b != 0x64 else '0')
    diff.append('1' if g != 0x95 else '0')
    diff.append('1' if r != 0x40 else '0')

b, g, r = (ord(fp.read(1)) for _ in range(3))
diff.append('1' if b != 0x61 else '0')
diff.append('1' if g != 0x94 else '0')
diff.append('1' if r != 0x3c else '0')

p1, p2 = (ord(fp.read(1)) for _ in range(2))
diff.append('1' if p1 != 0 else '0')
diff.append('1' if p2 != 0 else '0')

b, g, r = (ord(fp.read(1)) for _ in range(3))
diff.append('1' if b != 0x60 else '0')
diff.append('1' if g != 0x91 else '0')
diff.append('1' if r != 0x3c else '0')

b, g, r = (ord(fp.read(1)) for _ in range(3))
diff.append('1' if b != 0x64 else '0')
diff.append('1' if g != 0x95 else '0')
diff.append('1' if r != 0x40 else '0')

for i in range(46):
    b, g, r = (ord(fp.read(1)) for _ in range(3))
    diff.append('1' if b != 0x68 else '0')
    diff.append('1' if g != 0x99 else '0')
    diff.append('1' if r != 0x45 else '0')

b, g, r = (ord(fp.read(1)) for _ in range(3))
diff.append('1' if b != 0x65 else '0')
diff.append('1' if g != 0x98 else '0')
diff.append('1' if r != 0x41 else '0')

b, g, r = (ord(fp.read(1)) for _ in range(3))
diff.append('1' if b != 0x61 else '0')
diff.append('1' if g != 0x94 else '0')
diff.append('1' if r != 0x3c else '0')

p1, p2 = (ord(fp.read(1)) for _ in range(2))
diff.append('1' if p1 != 0 else '0')
diff.append('1' if p2 != 0 else '0')

ans = []
for i in range(len(diff) / 8):
    ans.append(chr(int(''.join(diff[i * 8:(i + 1) * 8])[::-1], 2)))
print ''.join(ans)

