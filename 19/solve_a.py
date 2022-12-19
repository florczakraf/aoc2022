import sys
import re
from dataclasses import dataclass
from queue import Queue
from copy import copy


class State:
    __slots__ = ("t", "ore", "clay", "obsidian", "geode", "ore_bots", "clay_bots", "obsidian_bots", "geode_bots")

    def __init__(self):
        self.t: int = 0
        self.ore: int = 0
        self.clay: int = 0
        self.obsidian: int = 0
        self.geode: int = 0
        self.ore_bots: int = 1
        self.clay_bots: int = 0
        self.obsidian_bots: int = 0
        self.geode_bots: int = 0

    def freeze(self):
        return (self.t, self.ore, self.clay, self.obsidian, self.geode, self.ore_bots, self.clay_bots, self.obsidian_bots, self.geode_bots)


def maximize_geode(bp, timeout):
    state = State()
    q = Queue()
    q.put(state)
    seen = set()
    max_score = 0

    while not q.empty():
        state = q.get()
        if state.freeze() in seen:
            continue
        seen.add(state.freeze())
        state.t += 1
        if state.t > timeout:
            max_score = max(max_score, bp[0] * state.geode)
            continue


        obsidian_bot_clay_cost = bp[4]
        geode_bot_obsidian_cost = bp[6]
        can_ore, can_clay, can_obsidian, can_geode = False, False, False, False
        if state.ore >= bp[1]: can_ore = True
        if state.ore >= bp[2]: can_clay = True
        if state.ore >= bp[3] and state.clay >= obsidian_bot_clay_cost: can_obsidian = True
        if state.ore >= bp[5] and state.obsidian >= geode_bot_obsidian_cost: can_geode = True

        state.ore += state.ore_bots
        state.clay += state.clay_bots
        state.obsidian += state.obsidian_bots
        state.geode += state.geode_bots

        if can_geode:
            next_state = copy(state)
            next_state.geode_bots += 1
            next_state.ore -= bp[5]
            next_state.obsidian -= geode_bot_obsidian_cost

            q.put(next_state)
            continue  # skip other paths if we can maximize geode

        if can_obsidian and state.obsidian_bots < geode_bot_obsidian_cost:
            next_state = copy(state)
            next_state.obsidian_bots += 1
            next_state.ore -= bp[3]
            next_state.clay -= obsidian_bot_clay_cost

            q.put(next_state)

        if can_clay and state.clay_bots < obsidian_bot_clay_cost:
            next_state = copy(state)
            next_state.clay_bots += 1
            next_state.ore -= bp[2]

            q.put(next_state)


        if can_ore and state.ore_bots < max(bp[1], bp[2], bp[3], bp[5]):
            next_state = copy(state)
            next_state.ore_bots += 1
            next_state.ore -= bp[1]

            q.put(next_state)


        q.put(state)  # just collect

    print(bp[0], max_score)
    return max_score





number = re.compile(r"\d+")
total = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")
    blueprint = list(map(int, number.findall(line)))
    total += maximize_geode(blueprint, 24)

print(total)
