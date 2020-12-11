import copy

# adjacent_index: [y_search, x_search]
_rules = {0: [-1, -1], 1: [-1, 0], 2: [-1, 1], 3: [0, -1], 4: [0, 1], 5: [1, -1], 6: [1, 0], 7: [1, 1]}


def maybe_keep_looking(x: int, y: int, map: list, adj: str, adj_index: int, rows: int, cols: int):
    y_dir, x_dir = _rules[adj_index][0], _rules[adj_index][1]
    y_change, x_change = y_dir * 2, x_dir * 2
    while adj == '.' and 0 < x + x_change < cols - 1 and 0 < y + y_change < rows - 1:
        adj = map[y + y_change][x + x_change]
        y_change += y_dir
        x_change += x_dir
    return adj


with open('input') as f:
    map_p1 = [['.'] + [s for s in r.strip('\n')] + ['.'] for r in f]

map_p1.insert(0, ['.'] * len(map_p1[0]))
map_p1.append(['.'] * len(map_p1[0]))
rows, cols = len(map_p1), len(map_p1[0])
map_p2 = copy.deepcopy(map_p1)
occ_sum_p1 = occ_sum_p2 = 0

while True:
    new_map_p1, new_map_p2 = copy.deepcopy(map_p1), copy.deepcopy(map_p2)
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            adj_p1 = map_p1[y - 1][x - 1:x + 2] + [map_p1[y][x - 1]] + [map_p1[y][x + 1]] + map_p1[y + 1][x - 1:x + 2]
            adj_p2 = map_p2[y - 1][x - 1:x + 2] + [map_p2[y][x - 1]] + [map_p2[y][x + 1]] + map_p2[y + 1][x - 1:x + 2]
            adj_p2 = [maybe_keep_looking(x, y, map_p2, adj, i, rows, cols) for i, adj in enumerate(adj_p2)]

            if map_p1[y][x] == 'L':
                new_map_p1[y][x] = '#' if adj_p1.count('#') == 0 else 'L'
            elif map_p1[y][x] == '#':
                new_map_p1[y][x] = 'L' if adj_p1.count('#') >= 4 else '#'

            if map_p2[y][x] == 'L':
                new_map_p2[y][x] = '#' if adj_p2.count('#') == 0 else 'L'
            elif map_p2[y][x] == '#':
                new_map_p2[y][x] = 'L' if adj_p2.count('#') >= 5 else '#'

    new_occ_sum_p1 = sum([r.count('#') for r in new_map_p1])
    new_occ_sum_p2 = sum([r.count('#') for r in new_map_p2])

    if new_occ_sum_p1 == occ_sum_p1 and new_occ_sum_p2 == occ_sum_p2:
        break  # probably faster here if I check for p1 and p2 separately, p2 converges a little faster

    map_p1, map_p2 = copy.deepcopy(new_map_p1), copy.deepcopy(new_map_p2)
    occ_sum_p1, occ_sum_p2 = new_occ_sum_p1, new_occ_sum_p2
print('part 1:', occ_sum_p1, '/ part 2:', occ_sum_p2)
