from PIL import Image
from string import maketrans, lowercase
im = Image.open('challenge.png')
pix = im.load()
lut = im.resize((256, 1))
lut.putdata(range(256))
lut = list(lut.convert("RGB").getdata())
for i, c in enumerate(lut):
    if not (c[0] == c[1] == c[2]):
        not_grey = i

binaries = []
for y in range(im.size[1]):
    for x in range(im.size[0]):
        if pix[x, y] == not_grey:
            binaries.append('1')
        else:
            binaries.append('0')

binaries = ''.join(binaries)

out = []
for i in range(len(binaries) / 8):
    out.append(chr(int(binaries[i * 8:(i + 1) * 8], 2)))

navajoes = ''.join(out).split()


navajo_dict = {'be-tkah':' '}
for line in open('navajo.txt'):
    alphabet, navajo, rest = filter(None, line.split())
    navajo_dict[navajo.lower()] = alphabet

ans = []
for nav in navajoes:
    ans.append(navajo_dict[nav])

s = ''.join(ans).split()[-1].lower()
fr = lowercase
to = lowercase[2:] + lowercase[:2]
print s.translate(maketrans(fr, to))
