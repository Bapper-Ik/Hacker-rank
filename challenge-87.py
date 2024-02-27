'''
Task


You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.
'''


import re

def validate_roman_numeral(s):
    pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
    return bool(re.match(pattern, s))

# Test cases
test_cases = ["III", "IV", "IX", "LVIII", "MCMXCIV", "MMMMCMXCIX", "ABC", "MMMXMM", "MCMCMCMC", ""]

for test_case in test_cases:
    print(f"{test_case}: {validate_roman_numeral(test_case)}")
