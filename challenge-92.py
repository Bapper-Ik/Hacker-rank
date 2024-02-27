''''
Task

You are given a 2-D array of size X.
Your task is to find:

1. The mean along axis 1
2. The var along axis 0
3. The std along axis None

'''



import numpy as np

# Input dimensions of the array
N, M = map(int, input().split())

# Input the array
arr = np.array([input().split() for _ in range(N)], dtype=int)

# Compute the mean along axis 1
mean_axis_1 = np.mean(arr, axis=1)

# Compute the var along axis 0 with ddof=1
var_axis_0 = np.var(arr, axis=0,)

# Compute the std along axis None
std_none = np.std(arr)

# Print the results with formatting
print(np.array2string(mean_axis_1, precision=11))
print(np.array2string(var_axis_0, precision=11))
if std_none == 0.0:
    print("{:.11f}".format(std_none))
else:
    print("{:.11f}".format(std_none))
