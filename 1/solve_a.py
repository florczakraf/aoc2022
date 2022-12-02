import sys


maximum = 0
current = 0

for line in sys.stdin.read().splitlines():
    if line:
        current += int(line)
    elif current > maximum:
        maximum = current
        current = 0
    else:
        current = 0

if current > maximum:
    maximum = current

print(maximum)
