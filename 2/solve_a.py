import sys

BEATS = {
    ("A", "Z"): "L",
    ("B", "X"): "L",
    ("C", "Y"): "L",
    ("A", "X"): "D",
    ("B", "Y"): "D",
    ("C", "Z"): "D",
}

POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "L": 0,
    "W": 6,
    "D": 3,
}

total = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    x, y = line.split()

    result = BEATS.get((x, y), "W")
    total += POINTS[y] + POINTS[result]

print(total)
