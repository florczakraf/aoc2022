import sys
import numpy as np

points = []

for line in sys.stdin.read().splitlines():
    #print(f" line: {line}")
    points.append(tuple(int(p) + 1 for p in line.split(",")))

points = np.array(points)
shape = np.max(points, axis=0) + 2
board = np.zeros(shape)
board[points[:,0], points[:, 1], points[:, 2]] = 1


def empty_neighbors(point):
    neighbors = []
    for i in range(3):
        for j in (-1, 1):
            neighbor = list(point)
            neighbor[i] += j
            if not board[tuple(neighbor)]:
                neighbors.append(neighbor)
    return len(neighbors)

total = 0
for point in points:
    total += empty_neighbors(point)

print(total)
