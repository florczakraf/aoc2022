import sys
from collections import deque

line = sys.stdin.read()
window = deque([*line[0:14]])
if len(set(window)) == 14:
    print(14)
    exit(0)
print(len(window))
for i, c in enumerate(line[14:], 15):

    window.popleft()
    window.append(c)
    if len(set(window)) == 14:
        print(i)
        break
