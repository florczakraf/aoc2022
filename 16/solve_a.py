import copy
import sys
import re
from queue import Queue

number = re.compile(r"-?\d+")
valve = re.compile("[A-Z]{2}")
valves = {}

for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    rate = int(number.findall(line)[0])
    found = valve.findall(line)
    current, paths = found[0], found[1:]
    valves[current] = {
        "rate": rate,
        "paths": paths
    }

considered = set()
init = {
    "time": 0,
    "opened": set(),
    "current": "AA",
    "pressure": 0,
    "path": ["AA"],
}
q = Queue()
q.put(init)
best = init
DEADLINE = 30

while not q.empty():
    state = q.get()

    to_consider = state["current"], state["pressure"]
    if to_consider in considered:
        continue
    considered.add(to_consider)

    if state["time"] == DEADLINE:
        continue

    current = state["current"]
    actions = []
    if current not in state["opened"] and valves[current]["rate"] > 0:
        actions.append(("open", current))
    for path in valves[current]["paths"]:
        actions.append(("visit", path))

    for action, valve in actions:
        future = copy.deepcopy(state)
        future["time"] += 1

        if action == "open":
            future["opened"].add(valve)
            future["pressure"] += (DEADLINE - future["time"]) * valves[valve]["rate"]
            future["path"].append(valve)

        else:
            if state["path"][-1] == valve:
                continue
            future["current"] = valve
            future["path"].append(valve)

        if future["pressure"] > best["pressure"]:
            best = future

        q.put(future)

print(best)
