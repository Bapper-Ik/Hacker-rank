'''
Task

You are given N mobile numbers. Sort them in ascending order then print them in the standard format shown below:
+91 xxxxx xxxxx

The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

debug the above code fragement to satisfy the description
'''



def wrapper(f):
    def fun(l):
        # Format the mobile numbers correctly before sorting and printing
        formatted_numbers = ['+91 ' + number[-10:-5] + ' ' + number[-5:] for number in l]
        # Sort the formatted numbers
        sorted_numbers = sorted(formatted_numbers)
        # Print the sorted numbers
        f(sorted_numbers)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


