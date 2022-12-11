import sys

xs = [1]
for line in sys.stdin.read().splitlines():
#    print(f" line: {line}")
    if line == "noop":
        xs.append(xs[-1])
    else:
        op, v = line.split()
        last = xs[-1]
        xs.append(last)
        xs.append(last + int(v))

pos = 0
for x in xs:
    if x - 1 <= pos <= x + 1:
        print("#", end="")
    else:
        print(".", end="")

    if pos == 39:
        pos = 0
        print()
    else:
        pos += 1
