import numpy as np
import matplotlib.pyplot as plt

imgs = {}
solutions = []

with open('input') as f:
    f = f.read().replace('Tile ', '').split('\n\n')
    for im in f:
        img = np.array([c for c in (im.split(':')[1].replace('\n', ''))]).reshape(10, 10)
        imgs[im.split(':')[0]] = img
        imgs[im.split(':')[0] + 'f'] = np.flip(img, 1)  # flip along "y" axis

ks = [k for k in imgs.keys()]
size = int((len(ks) / 2) ** 0.5)

for id in ks:
    imgs[id + 'R1'] = np.rot90(imgs[id])  # RN - rotated N times 90 degs CW so the dict sorts nicer
    imgs[id + 'R2'] = np.rot90(imgs[id + 'R1'])
    imgs[id + 'R3'] = np.rot90(imgs[id + 'R2'])

imgs = {id: imgs[id] for id in sorted([k for k in imgs.keys()])}
# 1: +y, 2: +x, 3: -y, 4: -x , reads in +x and +y
borders = {id: np.array([img[0], img[:, 9], img[9], img[:, 0]], dtype=np.dtype('U10')) for id, img in imgs.items()}
template = np.zeros((size, size), dtype=np.dtype('U10'))
candidates = []

for y in range(size):
    for x in range(size):
        if not x and not y:  # initialize candidates
            for id, border in borders.items():
                if 'f' in id:
                    ti = np.copy(template)
                    ti[0, 0] = id
                    candidates.append(ti)
            continue

        new_candidates = []
        for p1 in candidates:
            for id, border in borders.items():
                if any(id[:4] in cid for cid in p1.flatten()):
                    continue
                tc = np.copy(p1)
                if not x:
                    if not all(border[0, :] == borders[tc[y - 1, x]][2, :]):  # only compare up if x == 0
                        continue
                elif not y:
                    if not all(border[3, :] == borders[tc[y, x - 1]][1, :]):  # only compare left if y == 0
                        continue
                elif not all(border[3, :] == borders[tc[y, x - 1]][1, :]) or \
                        not all(border[0, :] == borders[tc[y - 1, x]][2, :]):  # else both up and left need to match
                    continue
                tc[y, x] = id
                new_candidates.append(tc)
        candidates = new_candidates[:]
        print('x: {}, y: {}, possible solutions: {}'.format(x, y, len(candidates)))
p1 = candidates[1]  # chose the 2nd solution since it matches the example
print('part 1:', int(p1[0, 0][:4]) * int(p1[0, size - 1][:4]) * int(p1[size - 1, 0][:4]) * int(p1[size - 1, size - 1][:4]))

# write out the image for p2
for y in range(size):
    for x in range(size):
        x_img = imgs[p1[y, x]][1:-1, 1:-1] if not x else np.concatenate((x_img, imgs[p1[y, x]][1:-1, 1:-1]), axis=1)
    p1_img = x_img if not y else np.concatenate((p1_img, x_img), axis=0)
np.savetxt('p2_input', p1_img, fmt="%s")

