import re
import numpy as np


dpt_indices, rules, nearby_tickets, score = [], [], [], []
is_mine = True

with open('input') as f:
    for i, l in enumerate(f):
        r = re.findall('(\d+)-(\d+)', l)
        if r:
            if 'departure' in l:
                dpt_indices.append(i)
            rules.append([range(int(l), int(h) + 1) for l, h in r] + [i])
            continue
        if 'nearby' in l:
            is_mine = False
        t = re.findall('(\d+)', l)
        if t:
            if is_mine:
                my_ticket = t
            else:
                invalids = [int(n) for n in t if all(int(n) not in sr for r in rules for sr in r[:-1])]
                if invalids:
                    score += invalids
                else:
                    nearby_tickets.append(tuple([int(n) for n in t]))

translate = {i: None for i in range(len(rules))}  # rule index : ticket index

while rules:
    for i in [t for t in range(len(my_ticket)) if t not in translate.values()]:
        col = [nt[i] for nt in nearby_tickets]
        match = [(p, r[-1]) for p, r in enumerate(rules) if all(any(n in sr for sr in r[:-1]) for n in col)]
        if len(match) == 1:
            translate[match[0][1]] = i
            rules.pop(match[0][0])

print('part 1:', sum(score))
print('part 2:', np.prod([int(my_ticket[translate[i]]) for i in dpt_indices]))
