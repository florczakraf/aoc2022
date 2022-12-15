import sys
import re


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


numbers = re.compile(r"-?\d+")
impossible = set()

# CONSIDERED_ROW = 10
CONSIDERED_ROW = 2_000_000

for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    sx, sy, bx, by = numbers.findall(line)
    s = (int(sx), int(sy))
    b = (int(bx), int(by))
    dist = distance(s, b)
    row_distance = distance(s, (s[0], CONSIDERED_ROW))
    if row_distance > dist:
        continue
    else:
        rest = abs(dist - row_distance)
        candidates = set(range(s[0] - rest, s[0] + rest + 1))
        if b[1] == CONSIDERED_ROW:
            candidates.discard(b[0])
        impossible.update(candidates)

print(len(impossible))
