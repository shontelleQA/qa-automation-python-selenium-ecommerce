"""
DEBUG SCRIPT: Verifying 100% coupon functionality

This script was used to debug issues with:
- Cart page not fully loading
- Hidden coupon input (modern WooCommerce block)
- Total not updating after coupon is applied

Includes:
- Step-by-step print statements
- Screenshot saving for visibility
- Explicit waits and fallbacks

Only for debugging. Final clean test lives in: test_verify_free_coupon.py

Test Case: Apply 100% Discount Coupon

🎯 Purpose:
Verify that applying a valid 100% discount coupon reduces the cart total to $0.00.

📝 Steps:
1️⃣ Add item to cart and click 'View cart'
2️⃣ Expand the 'Add a coupon' panel (if not already open)
3️⃣ Enter coupon and click Apply
4️⃣ Confirm cart total shows $0.00

📍 Tools:
- Selenium WebDriver
- WebDriverWait + Expected Conditions
- WooCommerce block cart logic
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

# Test variables
url_home = "http://localhost:8080"
coupon_code = "testcoupon"

try:
    print("🛒 Adding item to cart...")
    driver.get(url_home)

    add_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "add_to_cart_button")))
    add_btn.click()

    view_cart_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "added_to_cart")))
    view_cart_btn.click()
    print("🧾 Navigated to cart.")

    # Optional: small wait to let cart render fully
    time.sleep(1)

    print("🎟️ Expanding coupon section (if needed)...")
    toggle = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wc-block-components-panel__button")))
    if toggle.get_attribute("aria-expanded") == "false":
        toggle.click()
        print("✅ Panel expanded.")
    else:
        print("⚠️ Panel already open.")

    print("🔤 Entering coupon...")
    coupon_input = wait.until(EC.visibility_of_element_located((By.ID, "wc-block-components-totals-coupon__input-coupon")))
    coupon_input.clear()
    coupon_input.send_keys(coupon_code)

    print("🚀 Applying coupon...")
    apply_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wc-block-components-totals-coupon__button")))
    apply_btn.click()

    print("💰 Verifying total is $0.00...")
    total = wait.until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "wc-block-components-totals-footer-item-tax-value"),
        "$0.00"
    ))

    print("✅ PASS: Coupon applied successfully. Total is $0.00.")

except Exception as e:
    print(f"❌ FAIL: {e}")
    driver.save_screenshot("debug_coupon_error.png")

finally:
    time.sleep(3)
    driver.quit()
