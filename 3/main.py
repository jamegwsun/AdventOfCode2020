with open('input') as f:
    # slope: [index, trees]
    d = {1: [0, 0], 3: [0, 0], 5: [0, 0], 7: [0, 0], 0.5: [0, 0]}
    y_index = 0
    for line in f:
        for s, l in d.items():
            if s < 1 and y_index % int(1 / s):
                continue
            else:
                if line[int(l[0])] == '#':
                    l[1] += 1
                step = s if s >= 1 else 1
                l[0] = (l[0] + step) % (len(line) - 1)
        y_index += 1
    print("part 1:", d[3][1])
    print("part 2:", d[1][1] * d[3][1] * d[5][1] * d[7][1] * d[0.5][1])
