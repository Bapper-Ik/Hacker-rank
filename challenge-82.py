'''
Task


You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format:
The first line contains the string S.
The second line contains the string k.

Constraints:
1. 0 < len(S) < 100
2. 0 < len(K) < len(S)

Output Format:
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).


'''


# Input strings
S = input().strip()
k = input().strip()

# Initialize lists to store start and end indices
indices = []

# Find all occurrences of k in S
start_index = S.find(k)

# Iterate through the string to find all occurrences of k
while start_index != -1:
    end_index = start_index + len(k) - 1
    indices.append((start_index, end_index))
    start_index = S.find(k, start_index + 1)

# If no match is found, print (-1, -1)
if not indices:
    print((-1, -1))
else:
    # Print all found indices
    for index in indices:
        print(index)
