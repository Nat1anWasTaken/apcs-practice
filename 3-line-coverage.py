from typing import List

amount = int(input())

lines: List[range] = []

for _ in range(amount):
    line = input().split()
    lines.append(range(int(line[0]), int(line[1])))

sequence = [0] * max([line.stop for line in lines])

for line in lines:
    for number in line:
        sequence[number] = 1

print(sum(sequence))
