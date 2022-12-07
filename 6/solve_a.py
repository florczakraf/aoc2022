import sys
from collections import deque

line = sys.stdin.read()
window = deque([line[0], line[1], line[2], line[3]])
if len(set(window)) == 4:
    print(4)
    exit(0)

for i, c in enumerate(line[4:], 5):

    window.popleft()
    window.append(c)
    if len(set(window)) == 4:
        print(i)
        break
