'''
Task


Your task is to print an array of size NXM with its main diagonal elements as 1's and 0's everywhere else.

Note

In order to get alignment correct, please insert the line numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format:
A single line containing the space separated values of N and M.
N denotes the rows.
M denotes the columns.

Output Format:
Print the desired NXM array.
'''



import numpy as np

# Set legacy print option
np.set_printoptions(legacy='1.13')

# Read input
N, M = map(int, input().split())

# Create array with main diagonal elements as 1's and 0's everywhere else
arr = np.eye(N, M)

# Print the array
print(arr)
