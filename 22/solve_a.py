import sys
import re

fields = re.compile(r'.#')
moves = False
lines = []
max_len = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    if not line:
        moves = True
        continue

    if not moves:
        lines.append([])
        lines[-1].extend(line)
        max_len = max(max_len, len(line))
    else:
        moves = line
        break

row_starts, row_ends, col_starts, col_ends = [], [], [], []
for line in lines:
    if len(line) < max_len:
        line.extend(" " * (max_len - len(line)))

    for i, c in enumerate(line):
        if c == ' ':
            continue
        else:
            row_starts.append(i)
            break

    for i, c in enumerate(line[::-1]):
        if c == ' ':
            continue
        else:
            row_ends.append(max_len-i-1)
            break

for col in range(max_len):
    for row in range(len(lines)):
        c = lines[row][col]
        if c == " ":
            continue
        else:
            col_starts.append(row)
            break

    for row in range(len(lines)-1, -1, -1):
        c = lines[row][col]
        if c == " ":
            continue
        else:
            col_ends.append(row)
            break

print(row_starts)
print(row_ends)
print(col_starts)
print(col_ends)

def pl():
    for line in lines:
        print("".join(line))

def go_r(yx, n):
    y, x = yx
    for _ in range(n):
        orig_x = x
        x += 1
        if x == max_len or lines[y][x] == ' ':
            x = row_starts[y]
        if lines[y][x] == "#":
            return y, orig_x

    return y, x


def go_l(yx, n):
    y, x = yx
    for _ in range(n):
        orig_x = x
        x -= 1
        if x == -1 or lines[y][x] == ' ':
            x = row_ends[y]
        if lines[y][x] == "#":
            return y, orig_x

    return y, x


def go_d(yx, n):
    y, x = yx
    for _ in range(n):
        orig_y = y
        y += 1
        if y == len(lines) or lines[y][x] == ' ':
            y = col_starts[x]
        if lines[y][x] == "#":
            return orig_y, x

    return y, x


def go_u(yx, n):
    y, x = yx
    for _ in range(n):
        orig_y = y
        y -= 1
        if y == -1 or lines[y][x] == ' ':
            y = col_ends[x]
        if lines[y][x] == "#":
            return orig_y, x

    return y, x

directions = [go_r, go_d, go_l, go_u]

ops_re = re.compile(r"(R|L|\d+)")
yx = (0, row_starts[0])
direction = 0
for op in ops_re.findall(moves):
    if op == "R":
        print(op)
        direction = (direction + 1) % 4
    elif op == "L":
        print(op)
        direction = (direction - 1) % 4
    else:
        print(direction, int(op))
        yx = directions[direction](yx, int(op))
        print(f"{yx[0]} {yx[1]}")

y, x = yx
print(1000 * (y + 1) + 4 * (x + 1) + direction)
