'''
Task
You are given a positive integer . Print a numerical triangle of height N-1

Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

Note: Using anything related to strings will give a score of 0.

Input Format
A single line containing integer, N.

Constraints
1. 1 <= N <= 9
Output Format
Print N-1 lines as explained above.
'''


N = int(input())
for i in range(1, N): print(((10**i - 1) // 9) * i)