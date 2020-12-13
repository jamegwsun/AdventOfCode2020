from operator import mul
from functools import reduce


with open('input') as f:
    f = f.read().split('\n')
    d_min = int(f[0])
    buses = [(n, int(m)) for n, m in enumerate(f[1].split(',')) if m != 'x']

bus, dt = None, None
for _, b in buses:
    if dt is None or dt > int(b) - d_min % int(b):
        dt = int(b) - d_min % int(b)
        bus = b
print('part 1:', dt * bus)

# TIL Chinese Remainder Theorem
s = [None for i in range(len(buses))]
for i, (n, m) in enumerate(buses):
    s[i] = base = reduce(mul, [num for ind, num in buses if ind != n], 1)
    r = (m - n % m) if n else 0
    while s[i] % m != r:
        s[i] += base
print('part 2:', sum(s) % reduce(mul, [v for _, v in buses], 1))
