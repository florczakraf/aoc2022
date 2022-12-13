import sys
from itertools import zip_longest
import numpy as np
from functools import cmp_to_key

def cmp(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for (a_item, b_item) in zip_longest(a, b, fillvalue=None):
            if a_item is None:
                return -1
            if b_item is None:
                return 1
            result = cmp(a_item, b_item)
            if result != 0:
                return result
        return 0
    elif isinstance(a, list):
        return cmp(a, [b])
    elif isinstance(b, list):
        return cmp([a], b)
    else:
        return np.sign(a-b)

lines = sys.stdin.read().splitlines()
packets = [[[2]], [[6]]]
for i in range(0, len(lines), 3):
    index = i // 3 + 1
    a = eval(lines[i])
    b = eval(lines[i+1])
    packets.append(a)
    packets.append(b)

sorted_packets = sorted(packets, key=cmp_to_key(cmp))
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
