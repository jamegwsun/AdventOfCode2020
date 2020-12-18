def quick_maffs(m: list, p1: bool) -> int:
    for i, c in enumerate(m):  # solve ()
        if c == '(':
            for j in range(i+1, len(m)+1):
                if m[i+1:j].count('(') < m[i+1:j].count(')'):
                    m[i] = quick_maffs(m[i+1:j-1], p1)
                    for _ in range(j-i-1):
                        m.pop(i+1)
                    break
    for i, c in enumerate(m):  # solve +
        if c == '+':
            m[i+1] = m[i-1] + m[i+1]
            m[i-1:i+1] = None, None
        elif c == '*' and p1:
            m[i+1] = m[i-1] * m[i+1]
            m[i-1:i+1] = None, None
    m = [c for c in m if c]
    if not p1:
        for i, c in enumerate(m):  # solve *
            if c == '*':
                m[i+1] = m[i-1] * m[i+1]
                m[i-1:i+1] = None, None
    return m[-1]


with open('input') as f:
    maffs = [l.strip('\n').replace(" ", "") for l in f]

p1, p2 = [], []
for m in maffs:
    m = [int(c) if c in '1234567890' else c for c in m]
    p1.append(quick_maffs(m=m[:], p1=True))
    p2.append(quick_maffs(m=m[:], p1=False))
print(sum(p1))
print(sum(p2))
