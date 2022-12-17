import sys
from itertools import cycle
import numpy as np

blocks = cycle([
    np.array([[1, 1, 1, 1]]),
    np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
    np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]]),
    np.array([[1], [1], [1], [1]]),
    np.array([[1, 1], [1, 1]]),
])
jets = cycle(sys.stdin.read().strip())
tower = np.zeros((9001, 7))
jet_direction = {"<": -1, ">": 1}

def block_in_position(block, y, x):
    rows = []
    columns = []
    for i in range(block.shape[0]):
        for j in range(block.shape[1]):
            if block[i, j]:
                rows.append(y + i)
                columns.append(x + j)
    return rows, columns


height = 0
for _ in range(2022):
    block = next(blocks)
    y, x = height + 3, 2
    is_blocked = False

    while not is_blocked:
        direction = jet_direction[next(jets)]

        rows, columns = block_in_position(block, y, x + direction)
        if min(columns) >= 0 and max(columns) < 7 and np.all(tower[rows, columns] == 0):
            x += direction

        rows, columns = block_in_position(block, y - 1, x)
        if min(rows) < 0 or not np.all(tower[rows, columns] == 0):
            is_blocked = True
            tower[block_in_position(block, y, x)] = 1
            height = max(height, y + block.shape[0])
        else:
            y -= 1


print(height)
