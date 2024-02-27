'''
Task

You are given a set A and N other sets.
Your job is to find whether set A is a strict superset of each of the N sets.

Print ATrue, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

The first line contains the space separated elements of set A.
The second line contains integer N, the number of other sets.
The next N lines contains the space separated elements of the other sets.

Constraints:
1.  0 < len(set(A)) < 501
2. 0 < N < 21
3. 0 < len(otherSets) < 101

Output Format:
Print True if set A is a strict superset of all other N sets. Otherwise, print False.


'''

if __name__ == '__main__':
    # Elements of set A
    setA = set(map(int, input().split()))

    # Number of other sets
    N = int(input())

    # Initialize flag to True
    is_superset = True

    # Iterate through each other set
    for _ in range(N):
        # Elements of the other set
        other_set = set(map(int, input().split()))

        # Check if set A is a strict superset of the other set
        if not setA.issuperset(other_set):
            is_superset = False
            break

    # Print the result
    print(is_superset)

