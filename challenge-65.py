'''
Task

You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

Input Format
The first line contains a, the second line contains b, and the third line contains m.

Constraints
1. 1 <= a <= 10
2. 1 <= b <= 10
3. 2 <= m <= 1000
'''


if __name__ == "__main__":
    # Read the three integers
    a = int(input())
    b = int(input())
    m = int(input())

    # Print pow(a,b)
    print(pow(a, b))

    # Print pow(a,b,m)
    print(pow(a, b, m))
