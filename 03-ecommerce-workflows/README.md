# E-Commerce Workflow Tests

This directory contains UI automation tests focused on simulating and validating key user flows for an e-commerce site. It serves as a bridge between foundational Selenium skills and real-world test architecture.

## 📂 Folder Structure

- **raw-tests/** — Basic scripts that demonstrate individual workflows with minimal abstraction
- **automated-tests/** — Clean, reusable scripts following early-stage framework patterns (e.g., naming conventions, test case IDs)

## 🧪 Tech Stack

- Python 3.x
- Selenium WebDriver
- ChromeDriver (local browser automation)

## 🧭 Test Types

- Registration and login flows
- Coupon application and cart validation
- Full guest checkout (automated-tests only)

## 🚧 Future Enhancements

- Transition all raw tests into Page Object Model (POM)
- Introduce PyTest structure and fixtures
- Expand API coverage for back-end validation