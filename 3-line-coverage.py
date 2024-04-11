from typing import List

amount = int(input())

lines: List[range] = [range(int(line[0]), int(line[1])) for line in [input().split() for _ in range(amount)]]

sequence = set()

for line in lines:
    sequence.update(line)

print(len(sequence))
