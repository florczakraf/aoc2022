import sys
from collections import defaultdict
from pathlib import Path


dirs = defaultdict(int)
total = 0
cwd = Path("/")
dirs[cwd] = 0


def add_file(size, name):

    current = cwd
    dirs[Path("/")] += size

    while current != Path("/"):
        dirs[current] += size
        current = current.parent


for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    if line == "$ cd /":
        cwd = Path("/")
    elif line == "$ cd ..":
        cwd = cwd.parent
    elif line.startswith("$ cd"):
        cwd = cwd / line[5:]
    elif line == "$ ls":
        continue
    elif line.startswith("dir"):
        dirs[cwd / line[4:]] = dirs.get(cwd / line[4:], 0)
    else:
        size, name = line.split()
        add_file(int(size), name)

from pprint import pprint
pprint(dirs)
#print(sum(size for size in dirs.values() if size <= 100_000))
required = 30_000_000 - (70_000_000 - dirs[Path("/")])
#for path, size in sorted(dirs.items(), key=lambda x: x[1]):
#    if size >= required

print(next(item[1] for item in sorted(dirs.items(), key=lambda x: x[1]) if item[1] >= required))
