import sys
import heapq

map = []
S = None
E = None

def neighbors(v):
    y, x = v
    max_y = len(map)
    max_x = len(map[0])

    candidates = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    candidates = [c for c in candidates if 0 <= c[0] < max_y and 0 <= c[1] < max_x and map[c[0]][c[1]] <= map[y][x] + 1]

    return candidates


for row_index, line in enumerate(sys.stdin.read().splitlines()):
    map.append([])
    print(f" line: {line}")
    for column_index, c in enumerate(line):
        match c:
            case "S":
                map[-1].append(0)
                S = (row_index, column_index)
            case "E":
                map[-1].append(25)
                E = (row_index, column_index)
            case _:
                map[-1].append(ord(c) - ord("a"))


q = [S]
distances = {S: 0}
while q:
    cur = heapq.heappop(q)

    for n in neighbors(cur):
        candidate_distance = distances[cur] + 1
        if next_distance := distances.get(n):
            if next_distance <= candidate_distance:
                continue

        distances[n] = candidate_distance
        heapq.heappush(q, n)

print(distances[E])
