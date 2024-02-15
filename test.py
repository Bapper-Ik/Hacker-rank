

# stds = {
#     'baffa': 40,
#     'abba': 90,
#     'jdja': 20,
# }

# for key, value in stds:
#     print(key, value)


n = 7
m = 21

# for i in range(n):
#     for j in range(m):
#         print("_"*j)
#         if j == 10 & j == 12:
#             print(".", end='')
#             print('')
#         elif j == 11:
#             print("|")


# a = "this is a tes"
# new_a = a.split(' ')

# result = '-'.join(new_a)
# print(result)



# text = "ABCDCDC"

# sub = 'CDC'
# text_list = set(text)
# sub_list = set(sub)


# for i in range(len(sub_list)):
#     if sub_list[i] in text_list:
#         text_list.remove(sub_list[i])



S = 'qA2'

print(any(c.isalnum() for c in S))
print(any(c.isalpha() for c in S))
print(any(c.isdigit() for c in S))
print(any(c.islower() for c in S))
print(any(c.isupper() for c in S))
