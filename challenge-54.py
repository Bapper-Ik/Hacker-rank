'''
Task


You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.

Input Format:

The first line contains an integer N.N.  is the total number of integers in the list.
The second line contains the space separated list of N integers.

Constraints:
1. 0 < N < 100

Output Format:

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.
'''


def is_palindromic_integer(num):
    return str(num) == str(num)[::-1]

if __name__ == "__main__":
    N = int(input())
    integers = list(map(int, input().split()))

    # Check if all integers are positive
    all_positive = all(num > 0 for num in integers)

    # Check if any integer is palindromic
    any_palindromic = any(is_palindromic_integer(num) for num in integers)

    # Print the result
    print(all_positive and any_palindromic)
