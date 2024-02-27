'''
Task


You are given the coefficients of a polynomial P.
Your task is to find the value of P at point x.

Input Format:
The first line contains the space separated value of the coefficients in P.
The second line contains the value of x.

Output Format:
Print the desired value.
'''


def evaluate_polynomial(coefficients, x):
    result = 0
    for coef in coefficients:
        result = result * x + coef
    return result

# Input coefficients of the polynomial
coefficients = list(map(float, input().split()))

# Input value of x
x = float(input())

# Evaluate the polynomial at point x
result = evaluate_polynomial(coefficients, x)
print(result)

