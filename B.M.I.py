def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight_kg, height_m)

weight_category = interpret_bmi(bmi)

print(f"Your BMI is {bmi:.2f}, which indicates you are {weight_category}.")
