'''
Task

You have a non-empty set s, and you have to execute N commands given in N lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints
1. 0 < n < 20
2. 0 < N < 20

Output Format

Print the sum of the elements of set s on a single line.
'''


if __name__ == "__main__":
    # Read the number of elements in the set and the set itself
    n = int(input())
    s = set(map(int, input().split()))

    # Read the number of commands
    N = int(input())

    # Iterate through the commands
    for _ in range(N):
        # Read the command and its value
        command = input().split()
        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            s.remove(int(command[1]))
        elif command[0] == "discard":
            s.discard(int(command[1]))

    # Print the sum of the elements of the set
    print(sum(s))
