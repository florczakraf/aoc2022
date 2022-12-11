import sys
import numpy as np

visited = np.zeros((500, 500))
knots = np.array(((250, 250),) * 10)
visited[250, 250] = 1
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    direction, times = line.split()
    for i in range(int(times)):
        match direction:
            case "U":
                knots[0][0] += 1
            case "D":
                knots[0][0] -= 1
            case "L":
                knots[0][1] += 1
            case "R":
                knots[0][1] -= 1
        print()
        for j in range(1, 10):
            h = knots[j-1]
            t = knots[j]
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
        visited[knots[-1][0], knots[-1][1]] = 1

print(np.count_nonzero(visited))
