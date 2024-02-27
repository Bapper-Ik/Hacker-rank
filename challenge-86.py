

'''
Task



You are given a string s consisting only of digits 0-9, commas ,, and dots .

Your task is to complete the regex_pattern defined below, which will be used to re.split() all of the , and . symbols in s.

It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit.
'''


import re

# Input string
s = "100,000,000.000"

# Define the regular expression pattern to match commas and dots
regex_pattern = r'[,.]'

# Split the string using the regular expression pattern
split_result = re.split(regex_pattern, s)

# Print the split result as a single list




import re
print("\n".join(re.split(regex_pattern, input())))