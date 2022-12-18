import sys
import numpy as np
from queue import Queue

points = []

for line in sys.stdin.read().splitlines():
    #print(f" line: {line}")
    points.append(tuple(int(p) + 1 for p in line.split(",")))

points = np.array(points)
shape = np.max(points, axis=0) + 2
board = np.zeros(shape)
board[points[:,0], points[:, 1], points[:, 2]] = 1
visited = np.zeros(shape)
q = Queue()
q.put((0,0,0))
visited[(0,0,0)] = 1

def empty_neighbors(point):
    neighbors = []
    for i in range(3):
        for j in (-1, 1):
            neighbor = list(point)
            neighbor[i] += j
            if all(0 <= x < board.shape[n] for n, x in enumerate(neighbor)) and not board[tuple(neighbor)]:
                neighbors.append(tuple(neighbor))
    return neighbors


while not q.empty():
    el = q.get()
    for neighbor in empty_neighbors(el):
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            q.put(neighbor)

total = 0
for point in points:
    for neighbor in empty_neighbors(point):
        if visited[tuple(neighbor)]:
            total += 1

print(total)
