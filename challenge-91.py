

'''
Task


Neo has a complex matrix script. The matrix script is a  X  grid of strings. It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them. Neo reads the column from top to bottom and starts reading from the leftmost column.


Neo feels that there is no need to use 'if' conditions for decoding.

Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers N (rows) and M (columns) respectively.
The next N lines contain the row elements of the matrix script.

Constraints
0 < N,M < 100

Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script.
'''


import re

# Read input
N, M = map(int, input().split())
matrix = [input() for _ in range(N)]

# Transpose the matrix
transposed_matrix = list(zip(*matrix))

# Concatenate the transposed matrix into a single string
decoded_string = ''.join(''.join(column) for column in transposed_matrix)

# Replace symbols with spaces
decoded_string = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', decoded_string)

# Print the decoded string
print(decoded_string)
