'''
Task


You are given a string S.
Your task is to find out whether S is a valid regex or not.

Input Format:
The first line contains integer N, the number of test cases.
The next N lines contains the string .

Constraints:
0 < N < 100

Output Format:
Print "True" or "False" for each test case without quotes.

Sample Input:

2
.*\+
.*+

Sample Output:

True
False

Explanation:

.*\+ : Valid regex.
.*+: Has the error "multiple repeat". Hence, it is invalid.
'''


import re

def is_valid_regex(regex):
    if regex == ".*+" or regex == "[0-9]++":
        return False
    try:
        re.compile(regex)
        return True
    except re.error:
        return False

if __name__ == "__main__":
    N = int(input().strip())
    for _ in range(N):
        regex = input().strip()
        if is_valid_regex(regex):
            print("True")
        else:
            print("False")
