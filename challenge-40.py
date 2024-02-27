'''
Task

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

1. Print the three most common characters along with their occurrence count.
2. Sort in descending order of occurrence count.
3. If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

GOOGLE would have it's logo with the letters G, O, E.

Input Format:

A single line of input containing the string S.

Constraints:
1. 3 < len(S) <= 10^4
2. S has at least  distinct characters
Output Format:

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
'''


from collections import Counter

def top_three_characters(s):
    # Count the occurrences of each character in the string
    char_count = Counter(s)
    
    # Sort the characters by occurrence count in descending order
    # If occurrence count is the same, sort characters in alphabetical order
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top three characters along with their occurrence count
    for char, count in sorted_chars[:3]:
        print(char, count)

if __name__ == "__main__":
    s = input().strip()  # Input company name
    top_three_characters(s)
