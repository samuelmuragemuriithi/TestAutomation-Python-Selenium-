from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set the path to the ChromeDriver
driver_path = "E:/Downloads/TechnoBrian/chrome-headless-shell-win64/chrome-headless-shell-win64/chrome-headless-shell.exe"  # Replace with the actual path to your ChromeDriver

# Create a Service object
service = Service(driver_path)

# Initialize the Chrome WebDriver with the Service object
driver = webdriver.Chrome(service=service)

# Open a webpage
driver.get("https://www.google.com")

# Interact with the webpage
search_box = driver.find_element(By.NAME, "q")  # Find the search box using its name attribute
search_box.send_keys("Selenium Python")  # Type in the search query
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait for results to load (optional)
driver.implicitly_wait(10)

# Close the browser
driver.quit()
