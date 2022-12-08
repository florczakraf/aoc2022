import sys
import numpy as np

board = []

for line in sys.stdin.read().splitlines():
    board.append([])
    for c in line:
        board[-1].append(int(c))


board = np.array(board)
scores = np.zeros_like(board)

n = board.shape[0]

for row in range(1, n-1):
    for column in range(1, n-1):
        h = board[row, column]
        left = right = top = bottom = 0

        for i in range(column + 1, n):
            right += 1
            if board[row, i] >= h:
                break

        for i in range(column - 1, -1, -1):
            left += 1
            if board[row, i] >= h:
                break

        for i in range(row + 1, n):
            bottom += 1
            if board[i, column] >= h:
                break

        for i in range(row - 1, -1, -1):
            top += 1
            if board[i, column] >= h:
                break

        score = left * right * top * bottom
        scores[row, column] = score

print(scores.max())
