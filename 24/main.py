import re


def check_adjacent(init_loc: tuple, tiles: dict) -> int:  # returns num of black tiles
    adj_sum = 0
    new_tiles = {}
    for i in range(3):  # 0 - x, 1 - y, 2 - z
        for adj in [-1, +1]:
            l = list(init_loc)[:]
            l[(i+1) % 3] += adj
            l[(i+2) % 3] -= adj
            if tuple(l) in tiles.keys():
                adj_sum += tiles[tuple(l)]
            elif tiles[init_loc]:
                new_tiles[tuple(l)] = False
    return adj_sum, new_tiles  # adjacent sum, new populated tiles


with open('input') as f:
    f = f.readlines()

tiles = {}

for l in f:
    x, y, z = None, None, None  # ref: https://www.redblobgames.com/grids/hexagons/
    m = re.findall('(e|se|ne|w|sw|nw)', l)
    x = (m.count('e') - m.count('w')) + (m.count('ne') - m.count('sw'))  # e+ / ne+ -> x+
    y = (m.count('w') - m.count('e')) + (m.count('nw') - m.count('se'))  # w+ / nw+ -> y+
    z = (m.count('se') - m.count('nw')) + (m.count('sw') - m.count('ne'))  # se+ / sw+ -> z+
    tiles[(x, y, z)] = not (tiles[(x, y, z)]) if (x, y, z) in tiles.keys() else True
print('part 1:', sum([t for t in tiles.values() if t]))

# initialize new grid
new_tiles = {}
for loc, tile in tiles.items():
    new_tiles.update(check_adjacent(loc, tiles)[1])
tiles.update(new_tiles)

for d in range(100):
    flipped_tiles = tiles.copy()
    for loc, tile in tiles.items():
        adj_sum, new_tiles = check_adjacent(loc, tiles)
        flipped_tiles.update(new_tiles)
        if tile and (adj_sum > 2 or adj_sum == 0):
            flipped_tiles[loc] = False
        elif not tile and adj_sum == 2:
            flipped_tiles[loc] = True
            flipped_tiles.update(check_adjacent(loc, flipped_tiles)[1])  # expand grid around flipped tile
        else:
            flipped_tiles[loc] = tile
    tiles = flipped_tiles.copy()
    tiles.update(new_tiles)
print('part 2:', sum([t for t in tiles.values() if t]))
