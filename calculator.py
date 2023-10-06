def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y 

def multiply(x, y):
    return x * y 

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y 

def exponent(x, y):
    return x ** y 

def floor_divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x // y 

def calculator_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Floor Division")
    print("7. Quit") 

while True:
    calculator_menu()
    
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    if choice == '7':
        break
    
    if choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid input")
        continue
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", exponent(num1, num2))
    elif choice == '6':
        print("Result:", floor_divide(num1, num2))