from itertools import product

_rules, _exp_rules = {}, {}
msgs = []


def build_valids(i: int) -> list:
    if 'a' in _rules[i] or 'b' in _rules[i]:
        return _rules[i][0]
    else:
        valids = []
        for s in _rules[i]:
            v, p = [], []
            for c in s.split(' '):
                v.append(build_valids(int(c)))
            for j in range(len(v)):
                p = [''.join(c) for c in list(product(p, v[j]))] if p else v[j]
            valids += p
        if i in [31, 42]:
            _exp_rules[i] = valids
    return valids


with open('input') as f:
    for l in f:
        if ':' in l:
            index, rule = l.strip('\n').split(': ')
            _rules[int(index)] = rule.replace('\"', '').split(' | ')
        elif not l == '\n':
            msgs.append(l.strip('\n'))

build_valids(0)

valid_p1, valid_p2 = 0, 0
magic_len = len(_exp_rules[42][0])
print(_exp_rules[42])

for m in msgs:
    f_index, b_index = 0, 0
    m_segs = [m[i:i+magic_len] for i in range(0, len(m), magic_len)]
    while f_index < len(m_segs) and m_segs[f_index] in _exp_rules[42]:
        f_index += 1
    while b_index < len(m_segs) - 1 and m_segs[len(m_segs)-1-b_index] in _exp_rules[31]:
        b_index += 1
    if f_index + b_index == len(m_segs) and f_index > b_index and b_index:
        if len(m_segs) == 3:
            valid_p1 += 1
        valid_p2 += 1

print(valid_p1, valid_p2)
