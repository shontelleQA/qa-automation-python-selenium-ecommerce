"""
Test Case: Register New User

🎯 Purpose:
Verify that a new user can successfully register on the site and is automatically logged in.

📝 Steps:
1️⃣ Navigate to My Account page.
2️⃣ Generate a random email with domain @testlikeagirl.com and enter it with a fixed password.
3️⃣ Submit the registration form.
4️⃣ Confirm registration succeeded by checking that the Logout link appears.

📍 Tools:
- Selenium WebDriver
- Python random & string modules

Expected Result:
✅ Logout button is displayed after registration, meaning the user is logged in.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

# Setup: launch browser and set implicit wait
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Test variables
url = 'http://localhost:8080/my-account/'
email_field_id = 'reg_email'
password_field_id = 'reg_password'
register_button_css = 'button[value="Register"]'
logout_button_css = 'li.woocommerce-MyAccount-navigation-link--customer-logout a'
password = 'mynewpassword!1'

try:
    # Step 1: Navigate to the My Account page
    driver.get(url)

    # Step 2: Generate a random email address
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(15))
    random_email = random_string + '@testlikeagirl.com'

    # Step 3: Fill out the registration form
    email_field = driver.find_element(By.ID, email_field_id)
    email_field.send_keys(random_email)

    password_field = driver.find_element(By.ID, password_field_id)
    password_field.send_keys(password)

    # Step 4: Click the Register button
    register_button = driver.find_element(By.CSS_SELECTOR, register_button_css)
    register_button.click()

    # Step 5: Verify the Logout button is displayed
    logout_button = driver.find_element(By.CSS_SELECTOR, logout_button_css)

    if logout_button.is_displayed():
        print(f"✅ PASS: User '{random_email}' registered and logged in successfully.")
    else:
        raise Exception("❌ FAIL: Logout button not displayed — user may not be logged in.")

finally:
    # Optional: pause so you can see the result before browser closes
    time.sleep(3)
    driver.quit()
