'''
Task

You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the Kth attribute and print the final resulting table. Follow the example given below for better understanding.
Note that K is indexed from 0 to M-1, where M is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

Input Format:

The first line contains N and M separated by a space.
The next N lines each contain M elements.
The last line contains K.

Constraints:
1. 1 <= N, M <= 1000
2. 0 <=k < M
3. each element < = 1000

Output Format:

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

'''


    # Read inputs
N, M = map(int, input().split())
table = [input().split() for _ in range(N)]
K = int(input())

    # Sort the table based on the Kth attribute
table.sort(key=lambda x: int(x[K]))

    # Print the sorted table
for row in table:
    print(*row)
