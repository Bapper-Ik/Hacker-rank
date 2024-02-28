'''
Task


A valid email address meets the following criteria:

1. It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
2. The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
3. The domain and extension contain only English alphabetical characters.
4. The extension is 1, 2, or 3 characters in length.
Given  pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

'''


import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email))

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        name_email = input().strip()
        name, email = re.findall(r'(.*) <([^<>]+)>', name_email)[0]
        if is_valid_email(email):
            print(f"{name} <{email}>")
