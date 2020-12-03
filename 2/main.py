import re


valid_part1 = 0
valid_part2 = 0
with open('input') as f:
    for line in f:
        # 1-3 a: abcde
        m = re.match("(\d+)-(\d+) (\w): (\w+)", line)
        if m:
            if int(m.group(1)) <= m.group(4).count(m.group(3)) <= int(m.group(2)):
                valid_part1 += 1
            if (m.group(4)[int(m.group(1)) - 1] == m.group(3)) ^ (m.group(4)[int(m.group(2)) - 1] == m.group(3)):
                valid_part2 += 1
    print('part 1: {}, part 2: {}'.format(valid_part1, valid_part2))
