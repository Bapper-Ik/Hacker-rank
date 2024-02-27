'''
Task

You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A.

Note
In order to get the correct output format, add the line  below the numpy import.

Input Format

A single line of input containing the space separated elements of array .

Output Format

On the first line, print the floor of A.
On the second line, print the ceil of A.
On the third line, print the rint of A.

'''


import numpy as np

# Set the print options to print each element in a separate line
np.set_printoptions(sign=' ')

# Read the input array
A = np.array(input().split(), float)

# Print the floor, ceil, and rint of A
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))


