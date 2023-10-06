def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd" 

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True 

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1) 

num = int(input("Enter an integer: ")) 

print(f"{num} is {is_even_or_odd(num)}.") 

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime 

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")