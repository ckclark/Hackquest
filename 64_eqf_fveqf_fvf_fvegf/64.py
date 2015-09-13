lines = [x.strip() for x in open('64.txt').readlines()]
for shift in [16]: #range(len(lines[0])):
    out_graph = []
    for line in lines:
        out_line = []
        for i in range(len(line) - shift):
            if line[i] == line[i + shift]:
                out_line.append(' ')
            else:
                out_line.append('*')
        out_line = ''.join(out_line)
        out_graph.append(out_line)
    print shift
    print '\n'.join(out_graph)

