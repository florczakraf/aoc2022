import sys
from operator import add, mul
monkeys = []
lines = sys.stdin.read().splitlines()
mod = 1
for i in range(0, len(lines), 7):
    #print(f" line: {lines[i:i+7]}")
    items = [int(x) for x in lines[i+1].split(" ", maxsplit=4)[4].split(", ")]
    print(items)
    opline = lines[i+2].split(" ")
    if opline[-2] == "*":
        op = mul
    else:
        op = add

    operand = opline[-1]
    test = int(lines[i+3].split()[-1])
    mod *= test
    true = int(lines[i+4].split()[-1])
    false = int(lines[i+5].split()[-1])

    monkeys.append({"items": items, "op": op, "operand": operand, "test": test, "true": true, "false": false, "inspections": 0})
from pprint import pprint
pprint(monkeys)

for round in range(10000):
    for monkey in monkeys:
        monkey["inspections"] += len(monkey["items"])
        for item in monkey["items"]:
            item = monkey["op"](item, item if monkey["operand"] == "old" else int(monkey["operand"]))
            item %= mod
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)
        monkey["items"] = []


pprint(monkeys)
inspections = sorted([m["inspections"] for m in monkeys], reverse=True)
print(inspections)
print(inspections[0] * inspections[1])
