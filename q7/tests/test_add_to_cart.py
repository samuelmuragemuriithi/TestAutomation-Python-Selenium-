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
def test_add_single_item_to_cart():

    
    driver.get("https://www.your-ecommerce-site.com")
    
    # Find the product and add it to the cart
    product = driver.find_element(By.XPATH, "//div[@data-product-name='Product Name']")
    product.find_element(By.XPATH, ".//button[text()='Add to Cart']").click()

    # Verify that the cart count is updated
    cart_count = driver.find_element(By.ID, "cart-count")
    assert cart_count.text == "1", "Cart count did not update correctly."

    print("Test case passed: Add a Single Item to Cart")

# Call the function
test_add_single_item_to_cart()
