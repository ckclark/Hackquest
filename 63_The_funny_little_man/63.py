from PIL import Image, ImageSequence
from cStringIO import StringIO
import struct

fp = open('favicon.ico', 'rb')
fp.seek(38 + 40)
palette = []
for i in range(256):
    r, g, b, a = (ord(fp.read(1)) for _ in range(4))
    palette.append((b, g, r, a))

im = Image.new('RGBA', (32, 32))
pix = im.load()
for y in range(im.size[1] - 1, -1, -1):
    for x in range(im.size[0]):
        pixel = []
        color = ord(fp.read(1))
        pix[x, y] = palette[color]

for y in range(im.size[1] - 1, -1, -1):
    for x in range(4):
        alpha = ord(fp.read(1))
        for pixel in range(8):
            if alpha & (1 << (7 - pixel)):
                pix[x * 8 + pixel, y] = pix[x * 8 + pixel, y][:3] + (0,)
            else:
                pix[x * 8 + pixel, y] = pix[x * 8 + pixel, y][:3] + (255,)

im.save('img1.png')


fp.seek(2254 + 40)
palette = []
for i in range(16):
    r, g, b, a = (ord(fp.read(1)) for _ in range(4))
    palette.append((b, g, r, a))

im = Image.new('RGBA', (32, 32))
pix = im.load()
for y in range(im.size[1] - 1, -1, -1):
    for x in range(im.size[0] / 2):
        pixel = []
        c = ord(fp.read(1))
        color1 = (c >> 4) & 0xF
        color2 = c & 0xF
        pix[x * 2, y] = palette[color1]
        pix[x * 2 + 1, y] = palette[color2]

for y in range(im.size[1] - 1, -1, -1):
    for x in range(4):
        alpha = ord(fp.read(1))
        for pixel in range(8):
            if alpha & (1 << (7 - pixel)):
                pix[x * 8 + pixel, y] = pix[x * 8 + pixel, y][:3] + (0,)
            else:
                pix[x * 8 + pixel, y] = pix[x * 8 + pixel, y][:3] + (255,)

im.save('img2.png')


# only strange sequence: 'ujccnbpc', a Caesar cipher of 'funnyman'
