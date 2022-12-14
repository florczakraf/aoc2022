import sys
import numpy as np

source = (0, 500)
board = np.zeros((500, 1000))


def fill_rocks(coords):
    for i, (y, x) in enumerate(coords[1:], 1):
        y0, x0 = coords[i - 1]
        if x == x0:
            sign = np.sign(y0 - y)
            for y in range(y0, y - sign, -sign):
                board[y, x] = 1
        else:
            sign = np.sign(x0 - x)
            for x in range(x0, x - sign, -sign):
                board[y, x] = 1

max_y = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    coords = []
    for packed in line.split(" -> "):
        x, y = packed.split(",")
        coords.append((int(y), int(x)))
        max_y = max(max_y, int(y))
    fill_rocks(coords)

max_y += 2
board[max_y, :] = 1
print(max_y)

rest = 0
y, x = source
while True:
    if board[y+1, x] == 0:
        y += 1
    elif board[y+1, x-1] == 0:
        y += 1
        x -= 1
    elif board[y+1, x+1] == 0:
        y += 1
        x += 1
    else:
        board[y, x] = 1
        rest += 1

        if (y, x) == source:
            break

        y, x = source

print(rest)
