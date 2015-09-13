key = {
    1: 'RIAMLREK'[::-1],
    2: 'EFIFZWOP'[::-1],
    3: 'SKEPTINE'[::-1],
    4: 'GAOKECLD'[::-1],
    5: 'YMXARNFS'[::-1],
    6: 'SIATUGEF'[::-1],
}


input = [
    ['6+1', '1+3', '2-2', '3+1', '5+3', '4+1',],
    ['2+1', '1+3', '4+4', '3-4', '6-3', '5+0',],
    ['2-3', '3-2', '1-3', '5-3', '4+2', '6+2',],
]

for row in input:
    start = 7
    pos = {1:start, 2:start, 3:start, 4:start, 5:start, 6:start}
    ans = []
    for instr in row:
        n = int(instr[0])
        pos[n] = (pos[n] + int(instr[1:]) + 8) % 8
        ans.append(key[n][pos[n]])
    print ''.join(ans)

