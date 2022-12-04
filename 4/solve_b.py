import sys

total = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    first, second = line.split(",")
    first_a, first_b = first.split("-")
    second_a, second_b = second.split("-")
    first_set = set(range(int(first_a), int(first_b)+1))
    second_set = set(range(int(second_a), int(second_b)+1))

    intersection = first_set.intersection(second_set)

    if intersection:
        total += 1

print(total)
