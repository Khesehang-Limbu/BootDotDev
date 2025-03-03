"""
Factorial
Complete the factorial() function. It should calculate the factorial of a number. A factorial of a number is the product of all positive integers less than or equal to that number.

For example:

4! = 4 * 3 * 2 * 1 = 24

Note: In mathematics, the ! symbol denotes a factorial, but is not used in Python.

Tip: a Special Case for Zero
The value of 0! is 1. This keeps factorials consistent with the convention for an empty product.
"""

def factorial(num):
    factorial = 1
    if num == 0:
        return 1

    for i in range(1, num +1):
        factorial *= i
    return factorial
