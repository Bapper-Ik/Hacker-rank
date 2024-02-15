'''
Task
Given an integer,n , and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hask(t)
'''

n = int(input("Enter the number of integers: "))
integer_list = map(int, input("Enter the intgers: ").split())
my_tuple = tuple(integer_list)
hash_value = hash(my_tuple)
print(hash_value)
    

