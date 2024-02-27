'''
Task

Given 2 sets of integers, N and M, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either N or M but do not exist in both.

Input Format:
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.
'''

if __name__ == "__main__":
    # Input set M
    m = int(input())
    set_m = set(map(int, input().split()))

    # Input set N
    n = int(input())
    set_n = set(map(int, input().split()))

    # Calculate symmetric difference
    symmetric_difference = sorted(set_m.symmetric_difference(set_n))

    # Output symmetric difference
    for num in symmetric_difference:
        print(num)
