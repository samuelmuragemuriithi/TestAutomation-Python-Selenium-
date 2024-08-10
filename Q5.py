"""
5. Appium Automation:
Using Appium and Python, write a test script that automates a simple mobile application with the following 
steps:
 -Launches the application.
 -Logs in  using a predefined username and password.
 -Navigate to settings screen.
 Verifies that the user can update their profile information

 
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Desired capabilities for the mobile app and device/emulator
desired_caps = {
    "platformName": "Android",                # or "iOS" for iOS apps
    "deviceName": "emulator-5554",            # replace with your device name
    "app": "/path/to/your/app.apk",           # replace with the path to your .apk file or .ipa file
    "automationName": "UiAutomator2",         # or "XCUITest" for iOS apps
    "appPackage": "com.example.app",          # replace with your app's package name
    "appActivity": "com.example.app.MainActivity"  # replace with your app's main activity
}

# Initialize the WebDriver instance
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # Wait until the login screen is visible and interactable
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((MobileBy.ID, "com.example.app:id/username_field"))
    )

    # Log in using a predefined username and password
    driver.find_element(MobileBy.ID, "com.example.app:id/username_field").send_keys("your_username")
    driver.find_element(MobileBy.ID, "com.example.app:id/password_field").send_keys("your_password")
    driver.find_element(MobileBy.ID, "com.example.app:id/login_button").click()

    # Wait until the settings screen is accessible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, "Settings"))
    )

    # Navigate to the settings screen
    driver.find_element(MobileBy.ACCESSIBILITY_ID, "Settings").click()

    # Wait for the profile information fields to be visible
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((MobileBy.ID, "com.example.app:id/profile_name"))
    )

    # Update profile information
    driver.find_element(MobileBy.ID, "com.example.app:id/profile_name").clear()
    driver.find_element(MobileBy.ID, "com.example.app:id/profile_name").send_keys("New Name")

    driver.find_element(MobileBy.ID, "com.example.app:id/profile_email").clear()
    driver.find_element(MobileBy.ID, "com.example.app:id/profile_email").send_keys("newemail@example.com")

    # Save the updated profile information
    driver.find_element(MobileBy.ID, "com.example.app:id/save_button").click()

    # Verify that the update was successful (this could be a toast message, a confirmation dialog, etc.)
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((MobileBy.XPATH, "//*[contains(@text, 'Profile updated successfully')]"))
    )
    assert success_message.is_displayed(), "Profile update failed"

finally:
    # Quit the driver session
    driver.quit()
