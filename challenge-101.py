'''
Task


You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.
'''



import numpy

def arrays(arr):

    arr.reverse()    
    my_arr = numpy.array(arr, float)    
    return my_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)