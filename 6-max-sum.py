meta = input().split()
lines, _ = int(meta[0]), int(meta[1])

groups = [[int(number) for number in input().split()] for _ in range(lines)]

max_numbers = [max(group) for group in groups]
max_sum = sum(max_numbers)

divisible_numbers = []

for number in max_numbers:
    if max_sum % number == 0:
        divisible_numbers.append(number)

print(max_sum)
print(" ".join([str(number) for number in divisible_numbers]) or "-1")
