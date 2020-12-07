import re

bags = {'shiny gold'}
f = [l for l in open('input')]
finish = None

while not finish:
    finish = True
    for l in f:
        m = re.findall('(\w+ \w+) bag', l)
        contains_bags = set(m[1:])
        if contains_bags & bags:
            if m[0] not in bags:
                bags.add(m[0])
                finish = False
print(len(bags) - 1)

bags_instance = {'shiny gold': 1}
bags_total = 0
finish = None

while not finish:
    finish = True
    bags_temp = dict()
    for l in f:
        m = re.match('(\w+ \w+) bag', l)
        if m and m.group(1) in bags_instance.keys():
            m2 = re.findall('(\d) (\w+ \w+) bag', l)
            if m2:
                finish = False
                for q in m2:
                    if q[1] in bags_temp.keys():
                        bags_temp[q[1]] += int(q[0]) * bags_instance[m.group(1)]
                    else:
                        bags_temp[q[1]] = int(q[0]) * bags_instance[m.group(1)]
    bags_instance = bags_temp
    bags_total += sum(bags_instance.values())
print(bags_total)