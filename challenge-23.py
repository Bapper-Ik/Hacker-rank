'''
Task
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

'''


# def solve(s):
#     full_name = s.split(' ')
#     words = [full_name[i] for i in range(len(full_name))]

#     new_text = ''
#     for i in range(len(words)):
#         if not words[i][0].isalpha():
#             new_text += words[i].lower() + " "
#         elif words[i][0].isalpha():    
#             new_text += words[i].title() + " "  
#         elif( words[i] == ' '):
#             continue

    
#     return new_text


def capitalize_names(full_name):
    words = full_name.split()

    capitalized_words = [word.capitalize() for word in words]

    capitalized_full_name = ' '.join(capitalized_words)

    return capitalized_full_name

name = "alison heck"
capitalized_name = capitalize_names(name)
print(capitalized_name) 

