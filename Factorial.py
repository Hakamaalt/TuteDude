def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
