import sys
import re

stacks = []
reading_stacks = True
op_re = re.compile(r"move (\d+) from (\d+) to (\d+)")

def process_op(n, src, dst):
    tmp = []
    for i in range(n):
        tmp.append(stacks[src-1].pop())
    for v in tmp[::-1]:
        stacks[dst-1].append(v)

for line in sys.stdin.read().splitlines():
    print(f"   line: {line}")
    if reading_stacks:
        if not line:
            for i, stack in enumerate(stacks):
                stacks[i] = stack[::-1]
            reading_stacks = False
            continue

        n_stacks = (len(line) + 1) // 4
        if not stacks:
            for _ in range(n_stacks):
                stacks.append([])

        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stacks[i//4].append(line[i])

    else:
        result = op_re.match(line)
        print(result)
        process_op(int(result.group(1)), int(result.group(2)), int(result.group(3)))


from pprint import pprint
pprint(stacks)

print(''.join(stack.pop() for stack in stacks))

