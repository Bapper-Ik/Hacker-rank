'''
Task


You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

Input Format

A single line containing the space-separated integers.

Constraints
1. 1 < each integer <= 3

Output Format

First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.
'''



import numpy as np

# Read input shape
shape = tuple(map(int, input().split()))

# Print array using numpy.zeros
print(np.zeros(shape, dtype=int))

# Print array using numpy.ones
print(np.ones(shape, dtype=int))
