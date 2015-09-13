from PIL import Image
im = Image.open('pic.gif')
pix = im.load()
lut = im.resize((256, 1))
lut.putdata(range(256))
lut = list(lut.convert('RGB').getdata())
#for count, color in im.getcolors():
#    imOut = Image.new('RGB', im.size)
#    pixOut = imOut.load()
#    for x in range(im.size[0]):
#        for y in range(im.size[1]):
#            pixOut[x, y] = (255, 255, 255) if pix[x, y] == color else (0, 0, 0)
#    imOut.save('%d.png' % color)
seq = [18, 12, 16, 13, 14, 11, 15, 17, 16, 9, 10, 11]
ans = []
for c in seq:
    ans.append(chr(lut[c][1]))

print ''.join(ans)
