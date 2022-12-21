import sys
from graphlib import TopologicalSorter
from collections import defaultdict
from operator import add, mul, sub, truediv

ops = {
    "+": add,
    "*": mul,
    "-": sub,
    "/": truediv,
}

monkeys = {}
graph = defaultdict(set)
for line in sys.stdin.read().splitlines():
    name, task = line.split(": ")
    if task.isnumeric():
        monkeys[name] = int(task)
    else:
        a, op, b = task.split()
        monkeys[name] = (ops[op], a, b)
        graph[name].add(a)
        graph[name].add(b)

ts = TopologicalSorter(graph)
for name in ts.static_order():
    monkey = monkeys[name]
    try:
        monkeys[name] = monkey[0](monkeys[monkey[1]], monkeys[monkey[2]])
    except Exception:
        pass

print(monkeys["root"])

