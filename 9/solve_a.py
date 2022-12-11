import sys
import numpy as np

visited = np.zeros((500, 500))
h = np.array((250, 250))
t = np.array((250, 250))
visited[t[0], t[1]] = 1
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    direction, times = line.split()
    for i in range(int(times)):
        match direction:
            case "U":
                h[0] += 1
            case "D":
                h[0] -= 1
            case "L":
                h[1] += 1
            case "R":
                h[1] -= 1
        print()
        print(h, t)
        dist = np.linalg.norm(h-t)
        if dist > np.sqrt(2):
            if dist == 2:
                if h[0] < t[0]: t[0] -= 1
                elif h[0] > t[0]: t[0] += 1
                elif h[1] < t[1]: t[1] -= 1
                else: t[1] += 1
            else:
                diff = h - t
                if diff[0] < 0:
                    t[0] -= 1
                else: t[0] += 1

                if diff[1] < 0:
                    t[1] -= 1
                else: t[1] += 1
            print(f" -> {t}")
        visited[t[0], t[1]] = 1

print(visited[h[0], h[1]])
print(np.count_nonzero(visited))
