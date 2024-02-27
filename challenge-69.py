'''
Task

You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Input Format

The first line of input contains an integer N.
The next N lines contain credit card numbers.

Constraints
1. 0 < N < 100

Output Format

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.
'''



import re

def is_valid_credit_card(card_number):
    # Check if the card number starts with 4, 5, or 6
    if not re.match(r'^[456]', card_number):
        return False
    
    # Check if the card number contains exactly 16 digits
    if not re.match(r'^\d{4}-?\d{4}-?\d{4}-?\d{4}$', card_number):
        return False
    
    # Remove hyphens and join digits into a single string
    card_number = ''.join(card_number.split('-'))
    
    # Check if there are no 4 or more consecutive repeated digits
    if re.search(r'(\d)\1\1\1', card_number):
        return False
    
    return True

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        card_number = input().strip()
        if is_valid_credit_card(card_number):
            print("Valid")
        else:
            print("Invalid")
