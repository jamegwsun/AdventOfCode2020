import numpy as np


with open('input_p2') as f:
    f = [c for c in f.read().replace('\n', '').replace(' ', '')]
    size = int(len(f) ** 0.5)
    img = np.array(f).reshape(size, size)

sm = np.zeros((3, 20), dtype=str)
with open('sea_monster') as f:
    for i, l in enumerate(f):
        l = [c for c in l.strip('\n')]
        sm[i, 0:len(l)] = l
sm_indices = [i for i, c in enumerate(sm.flatten()) if c == '#']

imgs = [img]
for _ in range(3):
    imgs.append(np.rot90(imgs[-1]))

imgs.append(np.flip(img, 1))
for _ in range(3):
    imgs.append(np.rot90(imgs[-1]))

sm_y, sm_x = sm.shape

rough_total = dict(zip(*np.unique(img, return_counts=True)))['#']

for img in imgs:
    sm_sum = 0
    for y in range(size - sm_y):
        for x in range(size - sm_x):
            if all(t == '#' for t in [c for i, c in enumerate(img[y:y+sm_y, x:x+sm_x].flatten()) if i in sm_indices]):
                sm_sum += 1
    if sm_sum > 0:
        print('part 2:', rough_total - sm_sum * len(sm_indices))
