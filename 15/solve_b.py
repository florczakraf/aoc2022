import sys
import re
import z3


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


numbers = re.compile(r"-?\d+")

# MAX = 20
MAX = 4_000_000

solver = z3.Solver()
x = z3.Int("x")
y = z3.Int("y")
solver.add(x >= 0)
solver.add(y >= 0)
solver.add(x <= MAX)
solver.add(y <= MAX)

for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    sx, sy, bx, by = numbers.findall(line)
    s = (int(sx), int(sy))
    b = (int(bx), int(by))

    dist = distance(s, b)
    solver.add(z3.Abs(s[0] - x) + z3.Abs(s[1] - y) > dist)


print(solver.check())
model = solver.model()
print("x", model[x].as_long())
print("y", model[y].as_long())
print(model[x].as_long() * 4_000_000 + model[y].as_long())
