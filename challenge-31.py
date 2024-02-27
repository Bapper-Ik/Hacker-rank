'''
Task
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints:
1 <= len(string) <= 200

'''

def count_substring(string, substring):
    count = 0
    # Iterate over the string and count occurrences of the substring
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Input
string = input().strip()  # Original string
substring = input().strip()  # Substring

# Count occurrences of the substring in the string and print the result
print(count_substring(string, substring))


