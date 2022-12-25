import sys

values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "-": -1,
    "=": -2,
}

modulos = {
    0: "0",
    1: "1",
    2: "2",
    3: "=",
    4: "-",
}

total = 0
for line in sys.stdin.read().splitlines():
    print(f" line: {line}")

    position_multiplier = 1
    for c in line[::-1]:
        total += values[c] * position_multiplier
        position_multiplier *= 5

print(total)

snafu = []
while(total):
    digit = total % 5
    snafu.append(modulos[digit])
    total = total // 5 + (digit >= 3)

print("".join(snafu[::-1]))
