"""
2. Automation Script

Using Selenium WebDriver and Python, write a test script that performs the following actions on a web page-
 - Navigates to a login page
 - Enters a username and password
 - Clicks the login button.
 - Verifies that the user is redirected to a homepage and display a welcome message.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the WebDriver (Assuming Chrome in this example)
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("http://example.com/login")  # Replace with the actual login page URL

try:
    # Find the username and password fields and enter the credentials
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_field = driver.find_element(By.NAME, "password")

    username_field.send_keys("your_username")  # Replace with actual username
    password_field.send_keys("your_password")  # Replace with actual password

    # Find and click the login button
    login_button = driver.find_element(By.NAME, "login")  # Adjust if needed
    login_button.click()

    # Wait until the homepage is loaded and the welcome message is visible
    welcome_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "welcome-message"))  # Adjust as needed
    )

    # Verify the welcome message is displayed
    assert "Welcome" in welcome_message.text  # Adjust the text check if necessary

    print("Login successful, welcome message displayed.")

except TimeoutException:
    print("Login failed or welcome message not found.")
finally:
    # Close the browser
    driver.quit()
