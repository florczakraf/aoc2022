import sys
import numpy as np

board = []

for line in sys.stdin.read().splitlines():
    board.append([])
    for c in line:
        board[-1].append(int(c))


board = np.array(board)

left = np.zeros_like(board)
right = np.zeros_like(board)
top = np.zeros_like(board)
bottom = np.zeros_like(board)


n = board.shape[0]

for row in range(n):
    max_left = max_right = 0
    for column in range(n):
        left_is_visible = board[row, column] > max_left
        if left_is_visible:
            max_left = board[row, column]
            print(max_left)
            left[row, column] = 1

        right_is_visible = board[row, n-1-column] > max_right
        if right_is_visible:
            max_right = board[row, n-1-column]
            right[row, n-1-column] = 1

for column in range(n):
    max_top = max_bottom = 0
    for row in range(n):
        top_is_visible = board[row, column] > max_top
        if top_is_visible:
            max_top = board[row, column]
            top[row, column] = 1

        bottom_is_visible = board[n-1-row, column] > max_bottom
        if bottom_is_visible:
            max_bottom = board[n-1-row, column]
            bottom[n-1-row, column] = 1



from pprint import pprint
pprint(board)

pprint(left)
pprint(right)
pprint(top)
pprint(bottom)

ored = np.logical_or(np.logical_or(np.logical_or(left, right), top), bottom)
print(ored)
print(np.count_nonzero(ored[1:n-1, 1:n-1]))
print(2*n + 2 * (n-2) + np.count_nonzero(ored[1:n-1, 1:n-1]))
