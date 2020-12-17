import numpy as np


with open('input') as f:
    conv = [int(s) for s in list(f.read().replace('.', '0').replace('#', '1')) if s != '\n']

size = int(len(conv) ** 0.5)  # assume N x N input
iter = 6

grid_p1 = np.zeros((size + 2 * iter, size + 2 * iter, 1 + 2 * iter), dtype=np.int)
grid_p1[iter:iter + size, iter:iter + size, iter] = np.array(conv).reshape(size, size)
new_grid_p1 = np.copy(grid_p1)

grid_p2 = np.zeros((size + 2 * iter, size + 2 * iter, 1 + 2 * iter, 1 + 2 * iter), dtype=np.int)
grid_p2[iter:iter + size, iter:iter + size, iter, iter] = np.array(conv).reshape(size, size)
new_grid_p2 = np.copy(grid_p2)

xmax, ymax, zmax, wmax = grid_p2.shape

for i in range(iter):
    for x in range(xmax):
        for y in range(ymax):
            for z in range(zmax):
                neighbour_3d = grid_p1[max(0, x - 1):min(x + 2, xmax - 1),
                                       max(0, y - 1):min(y + 2, ymax - 1),
                                       max(0, z - 1):min(z + 2, zmax - 1)]
                nsum = np.sum(neighbour_3d) - grid_p1[x, y, z]
                if grid_p1[x, y, z]:
                    new_grid_p1[x, y, z] = 1 if nsum in (2, 3) else 0
                else:
                    new_grid_p1[x, y, z] = 1 if nsum == 3 else 0
                for w in range(wmax):
                    neighbour_4d = grid_p2[max(0, x - 1):min(x + 2, xmax - 1),
                                     max(0, y - 1):min(y + 2, ymax - 1),
                                     max(0, z - 1):min(z + 2, zmax - 1),
                                     max(0, w - 1):min(w + 2, wmax - 1)]
                    nsum = np.sum(neighbour_4d) - grid_p2[x, y, z, w]
                    if grid_p2[x, y, z, w]:
                        new_grid_p2[x, y, z, w] = 1 if nsum in (2, 3) else 0
                    else:
                        new_grid_p2[x, y, z, w] = 1 if nsum == 3 else 0
    grid_p1 = np.copy(new_grid_p1)
    grid_p2 = np.copy(new_grid_p2)

print(np.sum(grid_p1))
print(np.sum(grid_p2))