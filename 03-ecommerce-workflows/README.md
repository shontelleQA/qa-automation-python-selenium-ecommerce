# Raw Test Cases

This folder contains **scripted but unstructured test cases** for common e-commerce workflows.

These tests:
- Automate realistic scenarios (e.g., Register New User, Login with Invalid User, Verify Free Coupon)
- Use Selenium WebDriver + Python directly
- Do **not yet** use a formal test framework (like PyTest or Page Object Model)

🎯 **Purpose**
Demonstrate the ability to automate real-world workflows from scratch using Python & Selenium — before migrating to a maintainable framework.

---

## 📋 Test Cases

✅ **Register New User**
- Navigate to My Account page
- Generate a random email ending with `@testlikeagirl.com` and enter it with a fixed password
- Submit the registration form
- Verify that the Logout button appears (indicating user is logged in)

✅ **Login with Invalid User**
- [to be added]

✅ **Verify Free Coupon**
- [to be added]

---

## 📍 Notes
These tests are written as procedural scripts for clarity and learning purposes.
More advanced, maintainable tests will appear in the `automated-tests/` folder using a proper framework.

