''''
Task
Read in two integers,  and , and print three lines.
The first line is the integer division  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.

Input Format
The first line contains the first integer, a, and the second line contains the second integer, b.

Output Format
Print the result as described above.
'''


if __name__ == "__main__":
    # Read the two integers
    a = int(input())
    b = int(input())

    # Perform integer division
    print(a // b)

    # Print the result of the modulo operator
    print(a % b)

    # Print the divmod of a and b
    print(divmod(a, b))
