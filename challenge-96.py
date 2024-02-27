'''
Task


generate a python code that will enable user to write a N lines of text as an input. your task is to modify the user input, if a user uses "&&" replace it with "and" and if a user uses "||" replace it with "or".

constraints:
0 < N < 100

input format:
the first line contains the integer N. and the next N lines each contains a lines of text

output format:
output the modified text
'''



import re

# Read the number of lines
N = int(input())

# Read and modify each line of text
modified_text = []
for _ in range(N):
    line = input()
    modified_line = re.sub(r'(?<= )&&(?= )', 'and', line)
    modified_line = re.sub(r'(?<= )\|\|(?= )', 'or', modified_line)
    modified_text.append(modified_line)

# Print the modified text
for line in modified_text:
    print(line)
