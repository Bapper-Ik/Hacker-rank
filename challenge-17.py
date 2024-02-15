'''
Task

You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen

'''

def slpit_and_join(text):
    new_text = text.split(" ")
    result = '-'.join(new_text)

    return result


print(slpit_and_join("this is a test"))

