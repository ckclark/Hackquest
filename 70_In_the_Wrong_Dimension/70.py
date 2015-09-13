from PIL import Image
im = Image.open('file.jpg')
pix = im.load()
ans = []
print im.size
for i in range(im.size[0]):
    for j in range(im.size[1]):
        ans.append(chr(pix[i ,j]))
    ans.append('\n')
#print ''.join(ans)
