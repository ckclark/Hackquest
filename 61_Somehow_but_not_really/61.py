from PIL import Image
im = Image.open('diuzjbngda.gif')
pix = im.load()
for count, color in im.getcolors():
    imOut = Image.new('RGB', im.size)
    pixOut = imOut.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            if pix[x, y] == color:
                pixOut[x, y] = (255, 255, 255)
            else:
                pixOut[x, y] = (0, 0, 0)
    imOut.save('out%d.gif' % color)
