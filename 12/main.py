from math import sin, cos, radians, atan2, degrees, sqrt


def pos_to_angle(pos, w_pos):
    dist = [w - p for i, w in enumerate(w_pos) for j, p in enumerate(pos) if i == j]
    return degrees(atan2(dist[1], dist[0]))


def angle_to_pos(angle, pos, w_pos):
    dist = [w - p for i, w in enumerate(w_pos) for j, p in enumerate(pos) if i == j]
    return [cos(radians(angle)) * abs(sqrt(sum([d * d for d in dist]))) + pos[0],
            sin(radians(angle)) * abs(sqrt(sum([d * d for d in dist]))) + pos[1]]


with open('input') as f:
    instr = [l.strip('\n') for l in f]

_cdir = {'E': [1, 0], 'W': [-1, 0], 'S': [0, -1], 'N': [0, 1]}
_turn = {'L': 1, 'R': -1}

pos = [0, 0]  # x, y
angle = 0  # x, y

for s in instr:
    if s[0] in _cdir.keys():
        pos[0] += _cdir[s[0]][0] * int(s[1:])
        pos[1] += _cdir[s[0]][1] * int(s[1:])
    elif s[0] in _turn.keys():
        angle += _turn[s[0]] * int(s[1:])
    elif s[0] == 'F':
        pos[0] += cos(radians(angle)) * int(s[1:])
        pos[1] += sin(radians(angle)) * int(s[1:])

print('part 1:', int(sum([abs(p) for p in pos])))

pos = [0, 0]  # absolute
w_pos = [10, 1]  # absolute
w_angle = pos_to_angle(pos, w_pos)  # relative

for s in instr:
    if s[0] in _cdir.keys():
        w_pos[0] += _cdir[s[0]][0] * int(s[1:])
        w_pos[1] += _cdir[s[0]][1] * int(s[1:])
        w_angle = pos_to_angle(pos, w_pos)
    elif s[0] in _turn.keys():
        w_angle += _turn[s[0]] * int(s[1:])
        w_pos = angle_to_pos(w_angle, pos, w_pos)
    elif s[0] == 'F':
        move = [(w_pos[0] - pos[0]) * int(s[1:]), (w_pos[1] - pos[1]) * int(s[1:])]
        for i in [0, 1]:
            pos[i] += move[i]
            w_pos[i] += move[i]
        w_angle = pos_to_angle(pos, w_pos)

print('part 2:', sum([abs(p) for p in pos]))
