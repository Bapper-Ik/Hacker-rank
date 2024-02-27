'''
Task


You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 1. Number can start with +, - or . symbol.
 2. Number must contain at least 1 decimal value.
 3. Number must have exactly one . symbol.
 4. Number must not give any exceptions when converted using float(N).

Input Format:
The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Constraints:
1. 0 < T < 10

Output Format:
Output True or False for each test case.
'''




import re

# Read the number of test cases
T = int(input())

# Define the regular expression pattern for a valid float number
pattern = r'^[+-]?[0-9]*\.[0-9]+$'

# Iterate through each test case
for _ in range(T):
    # Read the input string
    N = input().strip()
    
    # Check if the input string matches the pattern for a valid float number
    is_valid = bool(re.match(pattern, N))
    print(is_valid)
