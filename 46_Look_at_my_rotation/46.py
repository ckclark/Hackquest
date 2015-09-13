from string import maketrans, lowercase
s = 'dmzgmiag'
fr = lowercase
for i in range(26):
    to = lowercase[i:] + lowercase[:i]
    tab = maketrans(fr, to)
    print s.translate(tab)

# veryeasy
