import re

# TODO rewrite part 1, clean the hell up

my_ticket = tuple()
dpt_pos, all_rules, nearby_tickets = [], [], []


def check_subrules(n: int, r: list):
    for sr in r:
        if n in sr:
            return True


with open('input') as f:
    is_mine = True
    for i, l in enumerate(f):
        r = re.findall('(\d+)-(\d+)', l)
        if r:
            if 'departure' in l:
                dpt_pos.append(i)
            all_rules.append([range(int(l), int(h) + 1) for l, h in r] + [i])
            continue
        elif 'nearby' in l:
            is_mine = False

        t = re.findall('(\d+)', l)
        if t:
            if is_mine:
                my_ticket = t
            else:
                for n in t:
                    is_valid = False
                    for r in all_rules:
                        for sr in r[:-1]:
                            if int(n) in sr:
                                is_valid = True
                    if not is_valid:
                        break
                if is_valid:
                    nearby_tickets.append(tuple([int(n) for n in t]))


convert_rules = {i: None for i in range(len(all_rules))}  # rule index : ticket index

for i in range(20):
    print('\n\n')
    for i in range(len(my_ticket)):
        col = [nt[i] for nt in nearby_tickets]
        match = [(p, r[-1]) for p, r in enumerate(all_rules) if all(check_subrules(n, r[:-1]) for n in col)]
        if len(match) == 1:
            convert_rules[match[0][1]] = i
            all_rules.pop(match[0][0])

answer = 1
for i, v in convert_rules.items():
    answer *= int(my_ticket[v])
    if i == 5:
        print(answer)