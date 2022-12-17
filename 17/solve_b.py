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
jets = sys.stdin.read().strip()
num_jets =len(jets)
tower = np.zeros((90001, 7), dtype=np.uint8)
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


seen = {}
height = 0
steps = 1_000_000_000_000
jet_offset = 0
for step in range(steps):
    block = next(blocks)
    y, x = height + 3, 2
    is_blocked = False
    previous_height = height
    while not is_blocked:
        direction = jet_direction[jets[jet_offset]]
        jet_offset += 1
        jet_offset %= num_jets

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

    growth = height - previous_height
    if old := seen.get((step % 5, jet_offset, growth)):
        old_height, old_step = old
        cycle = step - old_step
        diff = height - old_height
        if (steps - step) % cycle == 0:
            num_cycles = (steps - step) // cycle
            print(num_cycles * diff + height - 1)
            break
    else:
        seen[(step % 5, jet_offset, growth)] = height, step

