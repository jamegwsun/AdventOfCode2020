with open('input') as f:
    ip = [tuple(l.strip('\n').split(' = ')) for l in f]

mask, amask, mem_p1, mem_p2 = {}, {}, {}, {}
for l in ip:
    if l[0] == 'mask':
        mask = {len(l[1]) - i: int(m) for i, m in enumerate(l[1]) if m != 'X'}
        amask = {len(l[1]) - i: m for i, m in enumerate(l[1]) if m != '0'}
    else:
        # p1
        add = int(l[0][4:-1])
        val = int(l[1])
        vbin = bin(val)[2:]
        for d, m in mask.items():
            if d > len(vbin):
                val += 2 ** (d - 1) if m else 0
            elif vbin[len(vbin) - d] != str(m):
                val += 2 ** (d - 1) if m else - 2 ** (d - 1)
        mem_p1[add] = val

        # p2
        alist = [add]
        abin = bin(add)[2:]
        for d, m in amask.items():
            if m == 'X':
                alist += [a + 2 ** (d - 1) for a in alist] if d > len(abin) or abin[len(abin) - d] == '0' else \
                         [a - 2 ** (d - 1) for a in alist]
            else:
                alist = [a + 2 ** (d - 1) for a in alist] if d > len(abin) or abin[len(abin) - d] == '0' else alist
        mem_p2.update({a: int(l[1]) for a in alist})

print('part 1:', sum([v for v in mem_p1.values()]))
print('part 2:', sum([v for v in mem_p2.values()]))
