'''
Task
You are given a string S. Suppose a character ''c" occurs consecutively X times in the string. Replace these consecutive occurrences of the character ''c" with (X, c) in the string.

Input Format:
A single line of input consisting of the string .

Output Format:
A single line of output consisting of the modified string.

'''


my_str = input()

new_string = ''
counter = 1

for i in range(1, len(my_str)):
    if my_str[i] == my_str[i-1]:
        counter += 1
    else:
        new_string += f"({counter}, {my_str[i-1]})"
        counter = 1

new_string += f"({counter}, {my_str[i-1]})"
print(new_string)



