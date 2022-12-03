import sys

def value(item):
    if ord("a") <= ord(item) <= ord("z"):
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27

total = 0
for line in sys.stdin.read().splitlines():
    first, second = line[:len(line)//2], line[len(line)//2:]
    common = list(set(first) & set(second))[0]
    total += value(common)


print(total)
