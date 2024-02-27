'''
Task

You are given a string S.
Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string S.

Constraints:
1. 0 < len(S) < 100

Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input string
S = input().strip()

# Initialize a variable to store the repeating character
repeating_char = None

# Iterate over the characters in the string
for i in range(len(S) - 1):
    # Check if the current character is alphanumeric and has consecutive repetitions
    if S[i].isalnum() and S[i] == S[i + 1]:
        repeating_char = S[i]
        break

# Print the result
if repeating_char:
    print(repeating_char)
else:
    print(-1)
