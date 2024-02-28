

# # stds = {
# #     'baffa': 40,
# #     'abba': 90,
# #     'jdja': 20,
# # }

# # for key, value in stds:
# #     print(key, value)


# import os


# n = 7
# m = 21

# # for i in range(n):
# #     for j in range(m):
# #         print("_"*j)
# #         if j == 10 & j == 12:
# #             print(".", end='')
# #             print('')
# #         elif j == 11:
# #             print("|")


# # a = "this is a tes"
# # new_a = a.split(' ')

# # result = '-'.join(new_a)
# # print(result)



# # text = "ABCDCDC"

# # sub = 'CDC'
# # text_list = set(text)
# # sub_list = set(sub)


# # for i in range(len(sub_list)):
# #     if sub_list[i] in text_list:
# #         text_list.remove(sub_list[i])



# # S = 'qA2'

# # print(any(c.isalnum() for c in S))
# # print(any(c.isalpha() for c in S))
# # print(any(c.isdigit() for c in S))
# # print(any(c.islower() for c in S))
# # print(any(c.isupper() for c in S))



# # import string

# # letters = string.ascii_letters

# # print(letters)



# # def print_rangoli(size):
# #     import string
# #     alphabet = string.ascii_lowercase
# #     lines = []

# #     # Create the lines of the rangoli
# #     for i in range(size):
# #         s = "-".join(alphabet[i:size])
# #         lines.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

# #     # Print the rangoli in reverse order and then in the correct order
# #     for line in lines[::-1] + lines[1:]:
# #         print(line)

# # # Example usage
# # N = 5
# # print_rangoli(N)

# # import string

# # alphabet = string.ascii_lowercase
# # lines = []
# # size = 3
# # for i in range(size):
# #     s = "-".join(alphabet[i:size])
# #     lines.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

# # print(lines)


# # x = ['1','2','3','4','5']

# # for i in x[::-1]:
#     # print(i)
    
# # y = '-'.join(x)
# # print(y)

# def avg(*args):
#     total = sum(args)
#     return total / len(args)
    

# if __name__ == '__main__':
    
#     nums = map(int, input().split())
#     res = avg(*nums)
    
#     print('%.2f' % res + '\n')

