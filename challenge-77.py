'''
Task


You are given two integer arrays, A and B of dimensions NXM.
Your task is to perform the following operations:

1. Add (A + B)
2. Subtract (A - B)
3. Multiply (A * B)
4. Integer Division (A / B)
5. Mod (A % B)
6. Power (A ** B)

Note:
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format:
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.

Output Format:
Print the result of each operation in the given order under Task.
'''



import numpy as np

# Read input
N, M = map(int, input().split())

# Read arrays A and B
A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

# Perform operations
print(A + B)  # Addition
print(A - B)  # Subtraction
print(A * B)  # Multiplication
print(A // B) # Integer Division
print(A % B)  # Modulus
print(A ** B) # Power


