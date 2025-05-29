"""
Exercise: Basic Calculator Class

Create a class that has basic calculation methods: add, subtract, multiply, divide.
Demonstrates both simple method calls and constructor-based approach (v2).
"""

class BasicCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


# Usage example (version 1)
my_calc = BasicCalculator()
print(my_calc.add(2, 3))           # 5
print(my_calc.subtract(10, 4))     # 6

# --------------------------------------

class BasicCalculatorV2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y


# Usage example (version 2)
my_calc2 = BasicCalculatorV2(15, 11)
print(my_calc2.add())              # 26
