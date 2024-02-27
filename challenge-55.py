'''
Task

You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

1. All sorted lowercase letters are ahead of uppercase letters.
2. All sorted uppercase letters are ahead of digits.
3. All sorted odd digits are ahead of sorted even digits.

Input Format:
A single line of input contains the string S.

Constraints:
1. 0 < len(S) < 100

Output Format:
Output the sorted string S.
'''


def custom_sort(s):
    # Sort the string using custom key function
    return ''.join(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x)))

# Read the input string
s = input()

# Sort the string using custom sort function
sorted_s = custom_sort(s)

# Print the sorted string
print(sorted_s)
