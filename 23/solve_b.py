import sys
from collections import deque, defaultdict, Counter

directions = deque(["N", "S", "W", "E"])
neighbors = {
    "N": [(-1, 0), (-1, 1), (-1, -1)],
    "S": [(1, 0), (1, 1), (1, -1)],
    "W": [(0, -1), (1, -1), (-1, -1)],
    "E": [(0, 1), (1, 1), (-1, 1)],
}


def should_stop(board, elf):
    y, x = elf
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j == 0:
                continue
            if (y + i, x + j) in board:
                return False
    return True


board = set()
for y, line in enumerate(sys.stdin.read().splitlines()):
    print(f" line: {line}")
    for x, c in enumerate(line):
        if c == "#":
            board.add((y, x))

i = 1
while True:
    targets = {}
    counter = Counter()
    stay = set()

    for elf in board:
        if should_stop(board, elf):
            stay.add(elf)
            targets[elf] = elf
            continue

        y, x = elf
        for direction in directions:
            if all((y + dy, x + dx) not in board for (dy, dx) in neighbors[direction]):
                dy, dx = neighbors[direction][0]
                targets[elf] = (y + dy, x + dx)
                counter[(y + dy, x + dx)] += 1
                break
        else:
            targets[elf] = elf
            stay.add(elf)

    if len(board) == len(stay):
        print(i)
        break

    next_board = set()
    for elf in board:
        if counter[targets[elf]] == 1 or elf in stay:
            next_board.add(targets[elf])
        else:
            next_board.add(elf)
    board = next_board
    directions.rotate(-1)

    i += 1
