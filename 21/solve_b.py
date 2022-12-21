import sys
import z3

monkeys = {}
solver = z3.Solver()
humn = z3.Int("humn")
for line in sys.stdin.read().splitlines():
    name, task = line.split(": ")
    if name == "humn":
        monkeys[name] = "humn"
    elif task.isnumeric():
        monkeys[name] = task
    else:
        a, op, b = task.split()
        if name == "root":
            monkeys[name] = (a, "==", b)
        else:
            monkeys[name] = (a, op, b)


def make_expression(name):
    monkey = monkeys[name]
    if isinstance(monkey, tuple):
        a, op, b = monkey
        return f"({make_expression(a)} {op} {make_expression(b)})"
    else:
        return monkey


solver.add(eval(make_expression("root")))
print(solver.check())
print(solver.model()[humn].as_long())
