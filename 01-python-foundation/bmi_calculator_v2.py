"""
Improved BMI Calculator with formatted output and input handling
Includes examples of string formatting, rounding, and multiple print styles
"""

print("Welcome to BMI Calculator!!!")

# Take inputs as strings, convert later
weight = input("Enter your weight (kg): ")
height = input("Enter your height (m): ")

# Calculate BMI
bmi = float(weight) / (float(height) ** 2)
bmi = round(bmi, 1)

# Determine category and print result
if bmi <= 18.5:
    print("Your BMI is {}. You are Underweight.".format(bmi))
elif 18.5 < bmi <= 25:
    print(f"Your BMI is {bmi}. You are Normal.")
elif 25 < bmi <= 30:
    print(f"Your BMI is {bmi}. You are Overweight.")
else:
    print(f"Your BMI is {bmi}. You are Obese.")
