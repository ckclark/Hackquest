from string import maketrans
s = '''gmvb, dme ivjfpv ge khnv hu gmv mefpvp lhnvu ge gmvq yb gmvhi qzpgvip,
dhkk euv wzb khnv hu jivvweq, hu lizxv, zuw pzjv, jei zkk ghqvp.
jei jivvweq hp gmv ieeg jieq dmhxm aeb xzu lied, pe pgzuw fs jei befi ihlmgp,
yvxzfpv jivvweq hgpvkj hp wvihnvw jieq sedvi zuw qhlmg,
jvw yb gmv khjvp ej gmepv gmzg pfsseig hg pe gmvhi xmhkwivu qzb vuaeb hg dhgmefg jvzi.
gmvpv ziv gmv deiwp ej qb dziiheip sizbvi...
cuexc cuexc. dzcv fs uve!'''

fr = 'zuwkgmadfivbjpyqnlschxe'
to = 'andlthjwureyfsbmvgpkico'

l = zip(fr, to)
l.sort(key=lambda x:x[1])
print ''.join(x[0] for x in l)
print ''.join(x[1] for x in l)
tab = maketrans(fr, to)
for c in fr:
    s = s.replace(c, '^' + c + '_')

s = s.translate(tab)
print s.replace('^', '\x1b[31m').replace('_', '\x1b[m')

# hackquest
