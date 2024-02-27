'''
Task


For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, multiplication, division and modulus operations.

The real and imaginary precision part should be correct up to two decimal places.

Input Format

One line of input: The real and imaginary part of a number separated by a space.

Output Format

For two complex numbers C and D, the output should be in the following sequence on separate lines:
1. C + D
2. C - D
3. C * D
4. C / D
5. mod(C)
6. mod(D)

For complex numbers with non-zero real(A) and complex part (B), the output should be in the following format:
A + Bi
Replace the plus symbol (+) with a minus symbol (-) when .
B < 0
For complex numbers with a zero complex part i.e. real numbers, the output should be:
A + 0.00i
For complex numbers where the real part is zero and the complex part(B) is non-zero, the output should be:
0.00 + Bi

'''

import math

import math

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        if self.imag >= 0:
            return f"{self.real:.2f}+{self.imag:.2f}i"
        else:
            return f"{self.real:.2f}-{-self.imag:.2f}i"
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)
    
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)
    
    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imag ** 2), 0)



if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')