'''
Task

You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Note :
Vowels are defined as: AEIOU and aeiou.
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format:
A single line of input containing string 2.

Constraints:
1. 0 < len(S) < 100

Output Format:
Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print -1.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

# Input string
S = input().strip()

# Define regex pattern to match substrings with 2 or more vowels between consonants
pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])[aeiouAEIOU]{2,}(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'

# Find all matching substrings
matches = re.findall(pattern, S)

# Print the matches
if matches:
    for match in matches:
        print(match)
else:
    print(-1)


