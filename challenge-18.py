'''
Task
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello {first_name} {last_name}! You just delved into python.
'''


def message(first_name, last_name):
    print(f"Hello {first_name} {last_name}! You just delved into python.")


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

message(first_name, last_name)

