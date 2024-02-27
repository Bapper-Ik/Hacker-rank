'''
Task

 You are given some input, and you are required to check whether they are valid mobile numbers.

Input Format:

1. The first line contains an integer N, the number of inputs.
 2. N lines follow, each containing some string.

Constraints:
1. 1 <= N <= 10
2. 2 <= len(Number) <= 15

Output Format:

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.
'''


import re

def is_valid_mobile_number(number):
    # Define a regular expression pattern for a valid mobile number
    pattern = r'^[789]\d{9}$'
    
    # Use the match function to check if the number matches the pattern
    if re.match(pattern, number):
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    N = int(input())  # Number of inputs
    inputs = [input().strip() for _ in range(N)]  # List of input strings
    
    # Check each input string and print whether it is a valid mobile number or not
    for number in inputs:
        print(is_valid_mobile_number(number))
