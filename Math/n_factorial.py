# This program calculates the factorial of a number recursively
# Factorial of a number is its product with the numbers that come before it.
# For example, 5 factorial (denoted by 5!) is 5 x 4 x 3 x 2 x 1 = 120
# In the function we define a base case for recursion
# In this case, 0! or 1! is 1.
# For others, is just that number times the factorial of number before it

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)


print(Factorial(7))  # 7 x 6 x 5 x 4 x 3 x 2 x 1
print(Factorial(4))  # 4 x 3 x 2 x 1
