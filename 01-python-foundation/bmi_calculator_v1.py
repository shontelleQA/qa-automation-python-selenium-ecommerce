"""
Basic BMI Calculator
This version calculates BMI and uses if/else statements to determine weight category.
"""

# Take user input
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight / (height ** 2)

# Determine BMI category
if bmi <= 18.5:
    category = "Underweight"
elif bmi <= 25:
    category = "Normal"
elif bmi <= 30:
    category = "Overweight"
else:
    category = "Obese"

# Output result
print(f"Your BMI is {bmi:.1f}. You are {category}.")
