'''
Task
Read a given string, change the character at a given index and then print the modified string.

'''

def mutate_string(string, position, character):
    new_string = list(string)
    new_string[position] = character
    new_string = ''.join(new_string)
    
    return new_string


string = input("Enter any string: ")
index, char = input("Enter an index & character, seperate them with space: ").split()
new_string = mutate_string(string, int(index), char)
print(new_string)