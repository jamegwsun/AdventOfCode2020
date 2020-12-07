import re

f = [l for l in open('input')]
bags_p1 = {'shiny gold'}
bags_p2 = {'shiny gold': 1}
bags_p2_total = 0
finish = None

while not finish:
    finish = True
    bags_p2_inst = dict()
    for l in f:
        m = re.findall('(\w+ \w+) bag', l)
        # part 1
        contains_bags = set(m[1:])
        if contains_bags & bags_p1 and m[0] not in bags_p1:
            bags_p1.add(m[0])
            finish = False
        # part 2
        if m[0] in bags_p2.keys():
            m2 = re.findall('(\d) (\w+ \w+) bag', l)
            if m2:
                finish = False
                for q in m2:
                    if q[1] in bags_p2_inst.keys():
                        bags_p2_inst[q[1]] += int(q[0]) * bags_p2[m[0]]
                    else:
                        bags_p2_inst[q[1]] = int(q[0]) * bags_p2[m[0]]
    bags_p2 = bags_p2_inst
    bags_p2_total += sum(bags_p2.values())
print('part 1:', len(bags_p1) - 1, '/ part 2:', bags_p2_total)
