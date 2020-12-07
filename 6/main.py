f = open('input')
scores = [0, 0]  # p1, p2
for l in f.read().split('\n\n'):
    for i, p in enumerate(l.split('\n')):
        score_p2 = {q for q in p} if i == 0 else score_p2 & {q for q in p}
    scores[0] += len(({p for p in l} - {'\n'}))
    scores[1] += len(score_p2)
print("part 1:", scores[0], "part 2:", scores[1])
