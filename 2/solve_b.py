import sys

# X lose rock A      1  L
# Y draw paper B     2  D
# Z win scissors C   3  W

BEATS = {
    ("A", "X"): "W",
    ("A", "Y"): "L",
    ("A", "Z"): "D",
    ("B", "X"): "L",
    ("B", "Y"): "D",
    ("B", "Z"): "W",
    ("C", "X"): "D",
    ("C", "Y"): "W",
    ("C", "Z"): "L",
}

POINTS = {
    "L": 1,
    "D": 2,
    "W": 3,
    "X": 0,
    "Z": 6,
    "Y": 3,
}

total = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    x, y = line.split()

    result = BEATS[x, y]
    total += POINTS[y] + POINTS[result]

print(total)
