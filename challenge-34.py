'''
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format:

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Constraints:
0 < N <= 100

Output Format:

Print the space separated elements of deque .

'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

if __name__ == "__main__":
    N = int(input())  # Number of operations
    d = deque()  # Initialize an empty deque
    
    # Perform the specified operations
    for _ in range(N):
        operation = input().split()  # Read operation and its value
        if operation[0] == "append":
            d.append(operation[1])
        elif operation[0] == "pop":
            d.pop()
        elif operation[0] == "popleft":
            d.popleft()
        elif operation[0] == "appendleft":
            d.appendleft(operation[1])
    
    # Print the space-separated elements of deque
    print(*d)
