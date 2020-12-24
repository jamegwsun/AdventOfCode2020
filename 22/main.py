def play_game(p1: list, p2: list, part2: bool = False) -> int:  # winning player number
    hist = []
    while p1 and p2:
        round = p1 + ['-'] + p2
        if part2:
            if round in hist:
                return 1, p1, p2
            else:
                hist.append(round)

        if part2 and p1[0] <= len(p1[1:]) and p2[0] <= len(p2[1:]):
            winner, _, _ = play_game(p1[1:1+p1[0]], p2[1:1+p2[0]])
        else:
            winner = 2 if p1[0] < p2[0] else 1

        if winner == 1:
            p1 += [p1[0], p2[0]]
        elif winner == 2:
            p2 += [p2[0], p1[0]]
        p1.pop(0)
        p2.pop(0)
    return winner, p1, p2


with open('input') as f:
    f = f.read().split('Player')[1:]
    p1 = [int(c) for c in f[0].split('\n')[1:] if c != '']
    p2 = [int(c) for c in f[1].split('\n')[1:] if c != '']

_, p1_1, p2_1 = play_game(p1[:], p2[:])
print(sum((len(p1_1 + p2_1) - i) * c for i, c in enumerate(p1_1 + p2_1)))
_, p1_2, p2_2 = play_game(p1, p2, part2=True)
print(sum((len(p1_2 + p2_2) - i) * c for i, c in enumerate(p1_2 + p2_2)))
