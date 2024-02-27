'''
Task


You are given a NXM integer array matrix with space separated elements ( N= rows and  M= columns).
Your task is to print the transpose and flatten results.
'''


import numpy as np

# Input dimensions of the matrix
n, m = map(int, input().split())

# Input matrix elements
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert the matrix to a NumPy array
matrix_array = np.array(matrix)

# Print the transpose of the matrix
print(np.transpose(matrix_array))

# Print the flattened version of the matrix
print(matrix_array.flatten())
