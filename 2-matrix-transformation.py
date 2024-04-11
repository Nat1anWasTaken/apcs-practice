meta = input().split()

r, c, m = int(meta[0]), int(meta[1]), int(meta[2])

matrix = [[int(char) for char in input().split()] for _ in range(3)]

operations = [int(num) for num in input().split()]


def flip(matrix):
    return matrix[::-1]


def rotate(matrix):
    return [row for row in zip(*matrix[::-1])]


for operation in operations:
    if operation == 0:
        matrix = rotate(matrix)
    if operation == 1:
        matrix = flip(matrix)

print(len(matrix), len(matrix[0]))

for line in matrix:
    print(" ".join([str(num) for num in line]))
