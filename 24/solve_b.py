import heapq
import math
import sys
from collections import defaultdict
from copy import deepcopy
from itertools import chain
from queue import PriorityQueue


N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)
STAY = (0, 0)
dirs = {
    "^": N,
    "v": S,
    "<": W,
    ">": E,
}


class Field:
    def __init__(self, c):
        self.blizzards = []
        self.wall = False

        if c == "#":
            self.wall = True

        if c in dirs:
            self.blizzards.append(c)

    def __hash__(self):
        return hash(tuple((self.wall, *sorted(self.blizzards))))

    def __eq__(self, other):
        return hash(self) == hash(other)


board = []
end = start = None
lines = sys.stdin.read().splitlines()
for y, line in enumerate(lines):
    print(f" line: {line}")
    board.append([])
    for x, c in enumerate(line):
        if y == 0 and c == ".":
            start = (y, x)
        if y == len(lines) - 1 and c == ".":
            end = (y, x)

        board[-1].append(Field(c))


def dist(state, target):
    y0, x0 = state[0]
    y1, x1 = target
    return max(y0, y1) - min(y0, y1) + max(x0, x1) - min(x0, x1)


def is_legal(board, yx):
    y, x = yx

    if not (0 <= y < len(board) and 0 <= x < len(board[0])):
        return False

    if board[y][x].wall or board[y][x].blizzards:
        return False

    return True


def astar(state, target, boards):
    f_score = defaultdict(lambda: math.inf)
    g_score = defaultdict(lambda: math.inf)
    q = PriorityQueue()
    q.put((math.inf, state))
    states = {state}

    g_score[state] = 0
    f_score[state] = dist(state, target)

    while states:
        state = q.get()[1]
        states.remove(state)

        if dist(state, target) == 0:
            return g_score[state], state

        next_board_index = (state[1] + 1) % len(boards)
        next_board = boards[next_board_index]

        for (dy, dx) in (N, S, W, E, STAY):
            y, x = state[0]
            next_yx = y + dy, x + dx
            if not is_legal(next_board, next_yx):
                continue

            candidate_g_score = g_score[state] + 1
            next_state = (next_yx, next_board_index)
            if candidate_g_score < g_score[next_state]:
                g_score[next_state] = candidate_g_score
                f_score[next_state] = candidate_g_score + dist(state, target)
                if next_state not in states:
                    q.put((f_score[next_state], next_state))
                    states.add(next_state)


def generate_boards(board):
    previous_board = board

    while True:
        next_board = []
        for y, line in enumerate(previous_board):
            next_board.append([])
            for x, field in enumerate(line):
                if field.wall:
                    next_board[-1].append(Field("#"))
                else:
                    next_board[-1].append(Field("."))

        for y, line in enumerate(previous_board):
            for x, field in enumerate(line):
                for d in field.blizzards:
                    next_y = y + dirs[d][0]
                    next_x = x + dirs[d][1]

                    if next_y == len(board) - 1:
                        next_y = 1
                    elif next_y == 0:
                        next_y = len(board) - 2

                    if next_x == len(board[0]) - 1:
                        next_x = 1
                    elif next_x == 0:
                        next_x = len(board[0]) - 2

                    next_board[next_y][next_x].blizzards.append(d)

        previous_board = next_board
        yield next_board



boards_generator = generate_boards(board)


unique_boards = set()
boards = []
while tuple(chain.from_iterable(board)) not in unique_boards:
    boards.append(board)
    unique_boards.add(tuple(chain.from_iterable(board)))
    board = next(boards_generator)


print(len(boards))


state = (start, 0)
a, state = astar(state, end, boards)
b, state = astar(state, start, boards)
c, _ = astar(state, end, boards)

print(a+b+c)
