# Automated Test Scripts (Framework-Ready)

This folder contains clean, consistent test cases using naming conventions that map directly to test case IDs (e.g., `tcid_12`, `tcid_13`, etc). These scripts are structured to transition easily into a formal test framework.

## ✅ What's Included

- `test_tcid_12_verify_error.py` – Invalid login test
- `test_tcid_13_register_valid_user.py` – Valid user registration
- `test_tcid_33_guest_checkout.py` – Guest checkout with payment

## 🧠 Design Intent

- Scripts are readable and consistent
- Easy to integrate into PyTest, CI/CD, or extend with Page Objects
- Steps reflect real-world user behavior

## 🔜 Coming Soon

- Base classes for setup/teardown
- Test data externalization (YAML or JSON)
- Environment config and browser options