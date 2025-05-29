# Python Foundations for QA Automation

This section documents the Python programming fundamentals I practiced as part of my QA automation journey.

---

## ✅ Topics I’ve Covered 
- **Variables and Data Types** (strings, integers, booleans)
- **Lists and Dictionaries**
- **Control Flow**
  - Conditional logic (`if`, `elif`, `else`)
  - Loops (`for`, `while`)
- **Functions**
- **Exception Handling**
- **File I/O** (read/write to CSV)
- **Basic Debugging** using `pdb`
- **Random Data Generation**
- **Classes & Objects**
  - Writing custom classes
  - Using `__init__`, `self`, and methods
- **OOP Concepts**
  - Class inheritance (introduced)
  - Class composition (introduced)

---

## 💡 Real-World QA Use Cases
- Loops help iterate through test data or test steps
- Conditionals are the foundation of validation logic
- Exception handling is crucial when tests fail or data is missing
- File handling lets us read test data or write test logs

---

## 📌 Exercises I Wrote
- `basic_calculator_class.py` – class-based calculator using both method arguments and constructor attributes. This helped reinforce how classes and object methods work in Python, including `__init__`, `self`, and encapsulation.
- `bmi_calculator_v1.py` – basic version using if/else and f-string output  
- `bmi_calculator_v2.py` – improved version with `.format()`, rounding, and better UX  
- `even_number_checker.py` – checks if user input is even or not using modulus  
- `generate_random_emails.py` – simulates random email generation using dynamic strings and domain selection; output saved to CSV. This exercise reinforced working with loops, string manipulation, file writing, and randomness — all useful in data-driven testing.
- `process_products_exercises.py` – multiple logic exercises to filter and validate product data for a mock e-commerce platform


Each of these reinforces Python syntax and structure in a testable way.

---

## 🧠 Next Up
Now that the Python foundation is solid, I’m moving into:

- Setting up Selenium WebDriver with Python
- Writing browser automation scripts
- Testing real e-commerce workflows (locally hosted)
- Building reusable test functions and assertions

⚙️ Automation begins in `02-ui-automation-basics/` with foundational Selenium scripts and expands across structured folders:

- `03-ecommerce-workflows/` – real-world test cases like login, register, coupon use, and guest checkout
- `04-framework-design/` – building a maintainable test automation framework (POM, fixtures, utilities)
- `05-sql-validation/` – writing SQL queries to validate backend data tied to test scenarios
- `06-test-reports/` – generating HTML reports and capturing screenshots for failed tests
- `07-robot-framework/` – exploring keyword-driven testing with Robot Framework as a low-code automation layer
