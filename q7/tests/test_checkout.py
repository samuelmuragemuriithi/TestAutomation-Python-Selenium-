from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Chrome WebDriver
service = Service("path/to/chromedriver")
driver = webdriver.Chrome(service=service)

def test_proceed_to_checkout():
    driver.get("https://www.your-ecommerce-site.com")

    # Add an item to the cart first
    product = driver.find_element(By.XPATH, "//div[@data-product-name='Product Name']")
    product.find_element(By.XPATH, ".//button[text()='Add to Cart']").click()

    # Proceed to checkout
    driver.find_element(By.ID, "cart-icon").click()
    driver.find_element(By.XPATH, "//button[text()='Proceed to Checkout']").click()

    # Fill in the shipping and payment details
    driver.find_element(By.ID, "shipping-address").send_keys("123 Street Name, City, Country")
    driver.find_element(By.ID, "payment-method").send_keys("Credit Card")
    driver.find_element(By.ID, "card-number").send_keys("4111111111111111")
    driver.find_element(By.ID, "card-expiry").send_keys("12/25")
    driver.find_element(By.ID, "card-cvv").send_keys("123")

    # Place the order
    driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

    # Wait for confirmation
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "order-confirmation"))
    )

    assert "Order Confirmed" in confirmation_message.text, "Order was not confirmed."

    print("Test case passed: Proceed to Checkout")

# Call the function
test_proceed_to_checkout()
