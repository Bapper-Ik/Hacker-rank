import re

# Read the number of pairs
n = int(input())

# Read and process each pair
for _ in range(n):
    name, email = input().split()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(f'{name} <{email}>')
