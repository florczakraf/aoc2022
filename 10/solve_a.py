import sys

xs = [1]
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    if line == "noop":
        xs.append(xs[-1])
    else:
        op, v = line.split()
        last = xs[-1]
        xs.append(last)
        xs.append(last + int(v))
from pprint import pprint
pprint(list(zip(range(500), xs)))
print(sum(xs[i-1] * i for i in range(20, 222, 40)))
