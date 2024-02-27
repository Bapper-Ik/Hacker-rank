'''
Task


You are given two integer arrays of size NXP and MXP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

Input Format:
The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format:
Print the concatenated array of size (N + M)XP.
'''



import numpy as np

# Read input sizes
N, M, P = map(int, input().split())

# Read and concatenate arrays along axis 0
array1 = np.array([input().split() for _ in range(N)], dtype=int)
array2 = np.array([input().split() for _ in range(M)], dtype=int)
concatenated_array = np.concatenate((array1, array2), axis=0)

# Print concatenated array
print(concatenated_array)

