'''
Task
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

'''

def swap_case(text):
    new_text = ''
    for i in range(len(text)):
        if text[i].islower():
            char = text[i].upper()
            new_text += char
        else:
            char = text[i].lower()
            new_text += char
    return new_text

result = swap_case("Yakubu Musa Yakubu")

print(result)