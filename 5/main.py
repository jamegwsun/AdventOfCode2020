with open('input') as f:
    sids = []
    for l in f:
        row_lb = 0  # row lower bound
        col_lb = 0  # col lower bound
        rows = 128
        cols = 8
        for i in range(len(l)):
            if i < 7:
                rows /= 2
                if l[i] == 'B':
                    row_lb += rows
            else:
                cols /= 2
                if l[i] == 'R':
                    col_lb += cols
        sids.append(int(row_lb * 8 + col_lb))
    print('part 1:', max(sids))

    diff = 0
    for i, s in enumerate(sorted(sids)):
        if not diff == (s - i) and i > 0:
            print("part 2:", s - 1)
            break
        diff = s - i
