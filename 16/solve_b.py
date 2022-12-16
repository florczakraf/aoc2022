import copy
import sys
import re
from itertools import product
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
    "current": ["AA", "AA"],
    "pressure": 0,
    "path": [["AA"], ["AA"]],
}
q = Queue()
q.put(init)
best = init
DEADLINE = 26

while not q.empty():
    state = q.get()

    to_consider = tuple(sorted(state["current"])), state["pressure"]
    if to_consider in considered:
        continue
    considered.add(to_consider)

    if state["time"] == DEADLINE:
        continue

    actions = []
    for current in state["current"]:
        actions.append([])
        if current not in state["opened"] and valves[current]["rate"] > 0:
            actions[-1].append(("open", current))
        for path in valves[current]["paths"]:
            actions[-1].append(("visit", path))

    actions_set = set(product(*actions))

    for action_set in actions_set:
        future = copy.deepcopy(state)
        future["time"] += 1

        if action_set[0] == action_set[1] and action_set[0][0] == "open":
            continue

        for i, (action, valve) in enumerate(action_set):
            if action == "open":
                future["opened"].add(valve)
                future["pressure"] += (DEADLINE - future["time"]) * valves[valve]["rate"]
                future["path"][i].append(valve)

            else:
                if state["path"][i][-1] == valve:
                    continue
                future["current"][i] = valve
                future["path"][i].append(valve)

        if future["pressure"] > best["pressure"]:
            best = future

        q.put(future)

print(best)
