'''
Task
The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:

123.....n

Note that "...." represents the consecutive values in between.

'''


num = int(input("Enter any number: "))

for i in range(1, num+1):
    print(i, end='')

    