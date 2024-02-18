'''
Task

itertools.combinations_with_replacement(iterable, r)
This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Sample Code

Task:

You are given a string S.
Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.

Input Format:

A single line containing the string S and integer value K separated by a space.
'''


from itertools import combinations_with_replacement

S, K = input().split()
K = int(K)

comb = combinations_with_replacement(sorted(S), K)
for c in comb:
    print(''.join(c))
