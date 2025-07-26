# 🧪 Raw Test Cases

This folder contains **scripted but unstructured** test cases for common e-commerce workflows.

These tests:

- Automate realistic scenarios using **Selenium WebDriver + Python**
- Are written as **procedural scripts**
- Do **not** use a formal framework (e.g., PyTest or Page Object Model)

---

## 🎯 Purpose

Demonstrate the ability to automate real-world workflows from scratch using Python & Selenium  
— before migrating to a more maintainable structure.

---

## 📋 Test Cases

### ✅ Register New User
- Navigate to My Account page
- Generate a random email ending with `@testlikeagirl.com` and enter it with a fixed password
- Submit the registration form
- Confirm the Logout button appears (user is logged in)

### ✅ Login with Invalid User
- Navigate to My Account page
- Enter an invalid email and password
- Submit the login form
- Verify that the expected error message appears

### ✅ Verify Free Coupon
- Add an item to the cart from the homepage
- Click 'View Cart' to open the cart page
- Expand the “Add a coupon” section
- Enter a valid coupon and apply it
- Confirm cart total is reduced to `$0.00`

---

## 📍 Notes
These tests are written as procedural scripts for clarity and learning purposes.
More advanced, maintainable tests will appear in the `automated-tests/` folder using a proper framework.

- One debugging version of the `Verify Free Coupon` test is included to assist with troubleshooting.
- Clean versions are retained for portfolio display.
- Fully framework structured and reusable tests will be built in the `../automated-tests/` folder next.
