'''
Task
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Input Format

The first line contains the integer, N, the size of arr.
The second line contains the N space-separated integers, arr[i].

constraints:
0 < N <= 100

'''

def average(arr):
    # your code goes here
    distinct_heights = set(arr)
    
    # Calculate the sum of distinct heights
    sum_heights = sum(distinct_heights)
    
    # Calculate the average
    average = sum_heights / len(distinct_heights)
    
    return average

