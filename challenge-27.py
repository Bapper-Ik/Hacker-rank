'''
Task

itertools.combinations(iterable, r)
This tool returns the  length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task:

You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

Input Format:

A single line containing the string S and integer value K separated by a space.
'''


from itertools import combinations

S, K = input().split()
K = int(K)

for r in range(1, K + 1):
    comb = combinations(sorted(S), r)
    for c in comb:
        print(''.join(c))


