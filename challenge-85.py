'''
Task


You are given a 2-D array with dimensions NXM.
Your task is to perform the min function over axis 1 and then find the max of that.

Input Format

The first line of input contains the space separated values of N and M.
The next N lines contains M space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.

'''


import numpy as np

# Input dimensions of the array
N, M = map(int, input().split())

# Input the array
arr = np.array([input().split() for _ in range(N)], int)

# Compute the min along axis 1
min_axis_1 = np.min(arr, axis=1)

# Find the max of the min values
max_min_axis_1 = np.max(min_axis_1)

print(max_min_axis_1)
