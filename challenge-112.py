'''
Task

Given a list of rational numbers,find their product.
'''


from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = [Fraction(*map(int, input().split())) for _ in range(int(input()))]
    result = product(fracs)
    print(*result)

