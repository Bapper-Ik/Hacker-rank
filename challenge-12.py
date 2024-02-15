import numpy as np

N = int(input())

matrix = []

for _ in range(N):
    row = list(map(float, input().split()))
    matrix.append(row)

matrix = np.array(matrix)

determinant = np.linalg.det(matrix)

rounded_determinant = round(determinant, 2)

print(rounded_determinant)
