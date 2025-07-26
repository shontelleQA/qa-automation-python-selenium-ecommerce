"""
Test Case: Login With Invalid User

🎯 Purpose:
Verify that attempting to log in with an unregistered email shows the correct error message.

📝 Steps:
1️⃣ Navigate to My Account page.
2️⃣ Enter invalid email and password.
3️⃣ Submit the login form.
4️⃣ Verify the error message is displayed and matches the expected text.

📍 Tools:
- Selenium WebDriver

Expected Result:
❌ Login should fail and show: 'Unknown email address. Check again or try your username.'
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup: launch browser and set implicit wait
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Test variables
url = 'http://localhost:8080/my-account/'
email = 'abc@testlikeagirl.com'
password = 'abcdefge'
username_field_id = 'username'
password_field_id = 'password'
login_button_name = 'login'
error_msg_xpath = '//*[@id="content"]/div/div[1]/ul/li'
expected_error_msg = 'Unknown email address. Check again or try your username.'

try:
    # Step 1: Go to login page
    driver.get(url)

    # Step 2: Input invalid email and password
    driver.find_element(By.ID, username_field_id).send_keys(email)
    driver.find_element(By.ID, password_field_id).send_keys(password)

    # Step 3: Click Login
    driver.find_element(By.NAME, login_button_name).click()

    # Step 4: Capture and assert the error message
    actual_error = driver.find_element(By.XPATH, error_msg_xpath).text

    assert actual_error == expected_error_msg, f"❌ ERROR MISMATCH: Expected '{expected_error_msg}' but got '{actual_error}'"
    print(f"✅ PASS: Proper error message displayed for invalid user.")

finally:
    # Optional: pause so you can see the result before browser closes
    time.sleep(3)
    driver.quit()
