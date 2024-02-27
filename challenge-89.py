'''
Task

ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

1. It must contain at least 2 uppercase English alphabet characters.
2. It must contain at least 3 digits (0 - 9).
3. It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
4. No character should repeat.
5. There must be exactly 10 characters in a valid UID.

Input Format:
The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

def is_valid_uid(uid):
    # Rule 1: At least 2 uppercase English alphabet characters
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return False
    
    # Rule 2: At least 3 digits (0 - 9)
    if len(re.findall(r'\d', uid)) < 3:
        return False
    
    # Rule 3: Only contain alphanumeric characters (a - z, A - Z & 0 - 9)
    if not re.match(r'^[a-zA-Z0-9]{10}$', uid):
        return False
    
    # Rule 4: No character should repeat
    if len(set(uid)) != len(uid):
        return False
    
    return True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        uid = input().strip()
        if is_valid_uid(uid):
            print("Valid")
        else:
            print("Invalid")
