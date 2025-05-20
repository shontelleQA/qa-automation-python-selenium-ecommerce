"""
Even Number Checker

Write a program that takes an integer input and checks if it's an even number.
Prints 'True' if the number is even, 'False' if not.

Examples:
Input: 2 → Output: 2 is even → True
Input: 3 → Output: 3 is not even → False
"""

# Get user input
user_number = int(input("Please input a number to determine if it's even: "))

# Check if even
if user_number % 2 == 0:
    print("True")
else:
    print("False")
