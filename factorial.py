# WAP to find factorial of a number in python

def calculate_factorial(number):
    factorial = 1
    if number != 0:
        for _ in range(1, number+1):
            factorial *= _
    print(factorial)

calculate_factorial(5)

def calculate_factorial_recursive(number):
    if number == 0:
        return 1
    return number * calculate_factorial_recursive(number-1)

print(calculate_factorial_recursive(100))