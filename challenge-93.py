'''
Task

You are given two arrays A and B. Both have dimensions of NXM.
Your task is to compute their matrix product.

Input Format

The first line contains the integer N.
The next N lines contains N space separated integers of array A.
The following N lines contains N space separated integers of array B.

Output Format

Print the matrix multiplication of A and B.
'''


import numpy as np

# Read the value of N
N = int(input())

# Read array A
A = [list(map(int, input().split())) for _ in range(N)]

# Read array B
B = [list(map(int, input().split())) for _ in range(N)]

# Compute the matrix product using numpy
result = np.dot(A, B)

# Print the matrix product in the specified format
print(result)
