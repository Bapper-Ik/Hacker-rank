'''
Task

Read four numbers, , , , and , and print the result of .

Input Format
Integers , , , and  are given on four separate lines, respectively.


Output Format
Print the result of a^b + c^d on one line.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())

result = pow(a, b) + pow(c, d)
print(result)


