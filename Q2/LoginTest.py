from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the WebDriver (Assuming Chrome in this example)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("file:///E:/Downloads/TechnoBrian/TestAutomation-Python-Selenium-/indesQ2.html")  # Update with the local path to your HTML file

try:
    # Find the username and password fields and enter the credentials
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("your_username")  # Replace with actual username
    password_field.send_keys("your_password")  # Replace with actual password

    # Find and click the login button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    # Wait until the welcome message is visible
    welcome_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "welcome-message"))
    )

    # Print the actual text to debug
    print("Actual welcome message:", welcome_message.text)

    # Verify the welcome message is displayed
    assert "Welcome to the homepage!" == welcome_message.text

    print("Login successful, welcome message displayed.")

except TimeoutException:
    print("Login failed or welcome message not found.")
finally:
    # Close the browser
    driver.quit()
