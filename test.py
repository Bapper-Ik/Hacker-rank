

# stds = {
#     'baffa': 40,
#     'abba': 90,
#     'jdja': 20,
# }

# for key, value in stds:
#     print(key, value)


n = 7
m = 21

for i in range(n):
    for j in range(m):
        print("_"*j)
        if j == 10 & j == 12:
            print(".", end='')
            print('')
        elif j == 11:
            print("|")
            