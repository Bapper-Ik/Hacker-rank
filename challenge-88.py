'''
Task

'''


import re
from email.utils import parseaddr

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    n = int(input())
    emails = [input() for _ in range(n)]

    for email in emails:
        name, email = parseaddr(email)
        
        if is_valid_email(email):
            formatted_pair = f'"{name} <{email}>"'
            print(formatted_pair)
