"""
Debugging Example with pdb

This script simulates a simple bug and uses the Python debugger to step through the logic.
"""

import pdb

def calculate_discounted_price(price, discount):
    # Intentionally adding a bug: using + instead of -
    result = price + discount
    return result

# Simulate values
original_price = 100
discount = 20

# Set a breakpoint to investigate
pdb.set_trace()

final_price = calculate_discounted_price(original_price, discount)
print(f"The final price after discount is: ${final_price}")
