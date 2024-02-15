'''
Task
Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer  at position .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer .
4. append e: Insert integer  at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by  lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

'''
N = int(input())  # Read the number of commands

    # Initialize an empty list
my_list = []

    # Iterate through each command
for _ in range(N):
    command = input().split()  # Read the command
    operation = command[0]  # Get the operation

        # Perform the corresponding operation based on the command
    if operation == "insert":
        index = int(command[1])
        element = int(command[2])
        my_list.insert(index, element)
    elif operation == "print":
        print(my_list)
    elif operation == "remove":
        element = int(command[1])
        my_list.remove(element)
    elif operation == "append":
        element = int(command[1])
        my_list.append(element)
    elif operation == "sort":
        my_list.sort()
    elif operation == "pop":
        my_list.pop()
    elif operation == "reverse":
        my_list.reverse()
