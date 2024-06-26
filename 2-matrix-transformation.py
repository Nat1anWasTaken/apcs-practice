meta = input().split()

r, c, m = int(meta[0]), int(meta[1]), int(meta[2])

matrix = [[int(char) for char in input().split()] for _ in range(r)]

operations = [int(num) for num in input().split()]


def flip(matrix):
    return matrix[::-1]


def rotate(matrix):
    return [row for row in zip(*matrix[::-1])]


def rotate_anticlockwise(matrix):
    for i in range(3):
        matrix = rotate(matrix)

    return matrix


operations.reverse()

for operation in operations:
    if operation == 1:
        matrix = flip(matrix)
    if operation == 0:
        matrix = rotate_anticlockwise(matrix)

print(len(matrix), len(matrix[0]))

for line in matrix:
    print(" ".join([str(num) for num in line]))
