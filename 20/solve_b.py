import sys
from itertools import cycle, islice


def find_cycle(el):
    current = el
    yield el.v
    current = current.next
    while current.v != el.v:
        yield current.v
        current = current.next


class Node:
    def __init__(self, v, p=None, n=None):
        self.v: int = v
        self.prev: "Node" = p
        self.next: "Node" = n

nodes = []

first = None
prev = None
zero = None

for line in sys.stdin.read().splitlines():
    v = int(line) * 811589153
    n = Node(v, prev)

    if first is None:
        first = n

    if prev is not None:
        prev.next = n

    if v == 0:
        zero = n

    nodes.append(n)
    prev = n

n.next = first
first.prev = n

for i in range(10):
    print(i)
    for node in nodes:
        v = node.v
        if v == 0:
            continue

        current = node

        node.prev.next = node.next
        node.next.prev = node.prev

        iterations = abs(v) % (len(nodes) - 1)
        if v > 0:
            for _ in range(iterations):
                current = current.next
            node.next = current.next
            node.next.prev = node
            current.next = node
            node.prev = current

        if v < 0:
            for _ in range(iterations):
                current = current.prev
            node.next = current
            node.prev = current.prev
            current.prev = node
            node.prev.next = node

long_list = list(islice(cycle(find_cycle(zero)), 3001))
print((long_list[1000] + long_list[2000] + long_list[3000]))
