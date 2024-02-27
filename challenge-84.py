'''
Task


You are given a 2-D array with dimensions NXM.
Your task is to perform the sum tool over axis  and then find the product of that result.

Input Format

The first line of input contains space separated values of N and M.
The next N lines contains M space separated integers.

Output Format

Compute the sum along axis 0. Then, print the product of that sum.
'''


import numpy as np

# Input dimensions of the array
N, M = map(int, input().split())

# Input the array
arr = np.array([input().split() for _ in range(N)], int)

# Compute the sum along axis 0
sum_axis_0 = np.sum(arr, axis=0)

# Find the product of the sum
product = np.prod(sum_axis_0)

print(product)
