'''
Task


You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set .

Input Format

The first line contains the number of elements in set A.
The second line contains the space separated list of elements in set A.
The third line contains integer N, the number of other sets.
The next 2 * N lines are divided into N parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

constraints:
1. 0 < len(set(A)) < 1000
2. 0 < len(other(Sets) < 100
3. 0 < N < 100

Output Format:
Output the sum of elements in set A.


'''


if __name__ == "__main__":
    # Number of elements in set A
    n = int(input())
    
    # Set A
    set_a = set(map(int, input().split()))
    
    # Number of other sets
    n_sets = int(input())
    
    # Perform mutation operations on set A
    for _ in range(n_sets):
        operation, length = input().split()
        other_set = set(map(int, input().split()))
        
        if operation == "intersection_update":
            set_a.intersection_update(other_set)
        elif operation == "update":
            set_a.update(other_set)
        elif operation == "symmetric_difference_update":
            set_a.symmetric_difference_update(other_set)
        elif operation == "difference_update":
            set_a.difference_update(other_set)
    
    # Print the sum of elements in set A
    print(sum(set_a))
