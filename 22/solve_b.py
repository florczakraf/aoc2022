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

rights = {
    1: (2, 0),
    2: (7, 2),
    4: (2, 3),
    6: (7, 0),
    7: (2, 2),
    9: (7, 3),
}

lefts = {
    1: (6, 0),
    2: (1, 2),
    4: (6, 1),
    6: (1, 0),
    7: (6, 2),
    9: (1, 1),
}

ups = {
    1: (9, 0),
    2: (9, 3),
    4: (1, 3),
    6: (4, 0),
    7: (4, 3),
    9: (6, 3),
}
downs = {
    1: (4, 1),
    2: (4, 2),
    4: (7, 1),
    6: (9, 1),
    7: (9, 2),
    9: (2, 1),
}


def f(yx):
    y, x = yx
    return 3 * (y // 50) + x // 50

def l(yx):
    y, x = yx
    return y % 50, x % 50

def anchor(f):
    y = f // 3 * 50
    x = f % 3 * 50
    return y, x


def g(lyx, field, d=True):
    ly, lx = lyx
    ay, ax = anchor(field)
    gy = ay + ly
    gx = ax + lx
    if d:
        draw((gy, gx))
    return gy, gx


def transition(local_yx, from_direction, target):
    ly, lx = local_yx
    target_field, to_direction = target
    ay, ax = anchor(target_field)

    if from_direction == to_direction == 0:
        return (ay + ly, ax), to_direction

    if from_direction == to_direction == 2:
        return (ay + ly, ax + 49), to_direction

    if from_direction == 0 and to_direction == 2:
        return (ay + 49 - ly, ax + 49), to_direction

    if from_direction == to_direction == 1:
        return (ay, ax + lx), to_direction

    if from_direction == to_direction == 3:
        return (ay + 49, ax + lx), to_direction

    if from_direction == 0 and to_direction == 3:
        return (ay + 49, ax + ly), to_direction

    if from_direction == 1 and to_direction == 2:
        return (ay + lx, ax + 49), to_direction

    if from_direction == 2 and to_direction == 1:
        return (ay, ax + ly), to_direction

    if from_direction == 3 and to_direction == 0:
        return (ay + lx, ax), to_direction

    if from_direction == 2 and to_direction == 0:
        return (ay + 49 - ly, ax), to_direction

    raise RuntimeError(f"can't go from {from_direction} to {to_direction}")


def pl():
    for line in lines:
        print("".join(line))

directions = []


import numpy as np
base_img = np.zeros((len(lines), len(lines[0]), 3))
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "#":
            base_img[y, x] = (255, 0, 0)

img_id = 0
def draw(yx):
    # global img_id
    # import cv2
    # img = base_img.copy()
    # img[yx] = (0, 255, 0)
    #
    # cv2.imwrite(f"imgs/{img_id}.jpg", cv2.resize(img, (300, 400), interpolation=cv2.INTER_NEAREST))
    # img_id += 1
    pass


def go_r(yx, n):
    y, x = yx
    ly, lx = l(yx)

    field = f(yx)
    assert g((ly, lx), field) == yx, f"lyx: {ly, lx}, field {field}, g: {g((ly, lx), field)}, yx: {yx}"

    print("R", yx, n, field, l(yx))

    for i in range(n):
        orig_lx = lx
        orig_ly = ly
        draw(g((ly, lx), field))

        lx += 1
        if lx == 50:
            (ny, nx), nd = transition((orig_ly, orig_lx), 0, rights[field])
            if lines[ny][nx] != "#":
                draw((ny, nx))
                return directions[nd]((ny, nx), n-i-1)
            else:
                return g((orig_ly, orig_lx), field), 0
        gy, gx = g((ly, lx), field, d=False)
        if lines[gy][gx] == "#":
            return g((orig_ly, orig_lx), field), 0

    return g((ly, lx), field), 0


def go_l(yx, n):
    y, x = yx
    ly, lx = l(yx)

    field = f(yx)
    assert g((ly, lx), field) == yx, f"lyx: {ly, lx}, field {field}, g: {g((ly, lx), field)}, yx: {yx}"

    print("L", yx, n, field, l(yx))


    for i in range(n):
        orig_lx = lx
        orig_ly = ly
        draw(g((ly, lx), field))

        lx -= 1
        if lx == -1:
            (ny, nx), nd = transition((orig_ly, orig_lx), 2, lefts[field])
            if lines[ny][nx] != "#":
                draw((ny, nx))
                return directions[nd]((ny, nx), n-i-1)
            else:
                return g((orig_ly, orig_lx), field), 2
        gy, gx = g((ly, lx), field, d=False)
        if lines[gy][gx] == "#":
            return g((orig_ly, orig_lx), field), 2

    return g((ly, lx), field), 2

def go_d(yx, n):
    y, x = yx
    ly, lx = l(yx)

    field = f(yx)
    assert g((ly, lx), field) == yx, f"lyx: {ly, lx}, field {field}, g: {g((ly, lx), field)}, yx: {yx}"

    print("D", yx, n, field, l(yx))

    for i in range(n):
        orig_lx = lx
        orig_ly = ly
        draw(g((ly, lx), field))
        ly += 1
        if ly == 50:
            (ny, nx), nd = transition((orig_ly, orig_lx), 1, downs[field])
            if lines[ny][nx] != "#":
                draw((ny, nx))
                return directions[nd]((ny, nx), n-i-1)
            else:
                return g((orig_ly, orig_lx), field), 1
        gy, gx = g((ly, lx), field, d=False)
        if lines[gy][gx] == "#":
            return g((orig_ly, orig_lx), field), 1

    return g((ly, lx), field), 1


def go_u(yx, n):
    y, x = yx
    ly, lx = l(yx)

    field = f(yx)
    assert g((ly, lx), field) == yx, f"lyx: {ly, lx}, field {field}, g: {g((ly, lx), field)}, yx: {yx}"
    print("U", yx, n, field, l(yx))

    for i in range(n):
        orig_lx = lx
        orig_ly = ly
        draw(g((ly, lx), field))
        ly -= 1
        if ly == -1:
            (ny, nx), nd = transition((orig_ly, orig_lx), 3, ups[field])
            if lines[ny][nx] != "#":
                draw((ny, nx))
                return directions[nd]((ny, nx), n-i-1)
            else:
                return g((orig_ly, orig_lx), field), 3
        gy, gx = g((ly, lx), field, d=False)
        if lines[gy][gx] == "#":
            return g((orig_ly, orig_lx), field), 3

    return g((ly, lx), field), 3


directions.extend([go_r, go_d, go_l, go_u])


ops_re = re.compile(r"(R|L|\d+)")
yx = (0, 50)
direction = 0
for op in ops_re.findall(moves):
    if op == "R":
        # print(op)
        direction = (direction + 1) % 4
    elif op == "L":
        # print(op)
        direction = (direction - 1) % 4
    else:
        print()
        print(direction, int(op))
        yx, direction = directions[direction](yx, int(op))
        print(f"{yx[0]} {yx[1]}")

y, x = yx
print(1000 * (y + 1) + 4 * (x + 1) + direction)
