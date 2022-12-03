import sys

def value(item):
    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27

total = 0
lines = sys.stdin.read().splitlines()
for i in range(0, len(lines), 3):

    first, second, third = lines[i], lines[i+1], lines[i+2]
    common = list(set(first) & set(second) & set(third))[0]
    total += value(common)


print(total)
