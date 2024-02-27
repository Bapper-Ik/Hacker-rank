'''
Task


You are given two arrays: A and B.
Your task is to compute their inner and outer product.

Input Format:
The first line contains the space separated elements of array A.
The second line contains the space separated elements of array B.

Output Format:
First, print the inner product.
Second, print the outer product.
'''



import numpy as np

# Read array A
A = np.array(list(map(int, input().split())))

# Read array B
B = np.array(list(map(int, input().split())))

# Compute the inner product
inner_product = np.dot(A, B)

# Compute the outer product
outer_product = np.outer(A, B)

# Print the inner product
print(inner_product)

# Print the outer product
print(outer_product)
