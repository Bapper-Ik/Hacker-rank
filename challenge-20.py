'''
Task
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width W.

'''
import textwrap

def wrap(string, width):
    wraped_text = textwrap.fill(string, width)
    return wraped_text


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."

width = 50
result = wrap(text, width)

print(result)

