'''
Task
This tool computes the cartesian product of input iterables.
It is equivalent to nested for-loops.
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

You are given a two lists A andB . Your task is to compute their cartesian product AXB.

nput Format

The first line contains the space separated elements of list A.
The second line contains the space separated elements of list B.

Both lists have no duplicate integer elements.

'''


from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

cartesian_product = list(product(A, B))

for pair in cartesian_product:
    print(pair, end=' ')



