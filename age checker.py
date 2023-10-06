from datetime import datetime

birthdate_str = input("Enter your birthdate (yyyy-mm-dd): ")

birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

current_date = datetime.now()

age = current_date.year - birthdate.year - ((current_date.month, current_date.day) < (birthdate.month, birthdate.day))

print(f"Your age is {age} years.")
