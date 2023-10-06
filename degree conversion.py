def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def temperature_converter_menu():
    print("Select temperature conversion:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Quit")

while True:
    temperature_converter_menu()
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '3':
        break
    
    if choice not in ('1', '2'):
        print("Invalid input")
        continue
    
    temperature = float(input("Enter temperature: "))
    
    if choice == '1':
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C")
    elif choice == '2':
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F")
