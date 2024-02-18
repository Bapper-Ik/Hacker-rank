'''
Task


'''

def average(array):
    # your code goes here
    total = sum(array)
    avg =  "{:.3f}".format(total / float(len(array)))
    
    return avg
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)