'''
Task
itertools.permutations(iterable[, r])

This tool returns successive  length permutations of elements in an iterable.

If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

Task:

You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

Input Format:

A single line containing the space separated string S and the integer value K.


'''


from itertools import permutations

S, K = input().split()
K = int(K)

perms = sorted(permutations(S, K))
for perm in perms:
    print(''.join(perm))


