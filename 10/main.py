import re

_rules = {}


def do_the_counting_thing(length: int):
    if length in [-1, 0]:
        return 1
    elif length in _rules.keys():
        return _rules[length]
    combo = 0
    bin_range = [0, int('0b' + '1' * length, 2) + 1]
    for n in range(bin_range[0], bin_range[1]):
        combo += 1 if not re.match('[1]{3,}?', str(bin(n))[2:]) else 0  # 1 indicates skipping adapter
    _rules[length] = combo
    return combo


with open('input') as f:
    adapters = sorted([int(l) for l in f] + [0])
diffs = [adapters[i] - adapters[i - 1] for i in range(1, len(adapters))] + [3]

s = -1  # -1 because of some weird indexing thing
sum = 1
for i, d in enumerate(diffs):
    if d == 3:
        sum *= do_the_counting_thing(i - s - 2)  # (i - s - 2) is the # of skippable adapters
        s = i

print('part 1:', diffs.count(1) * diffs.count(3), 'part 2:', sum)
