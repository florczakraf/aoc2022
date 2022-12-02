import sys

current = 0
sums = []
for line in sys.stdin.read().splitlines():
    if line:
        current += int(line)
    else:
        sums.append(current)
        current = 0
sums.append(current)

print(sum(sorted(sums)[-3:]))
