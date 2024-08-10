"""
4. Selenium Automation:
 Write a selenium  WebDriver Script in Python  that perform the following actions:
  -Opens a browser and navigates to a search engine (e,g., Google).
  -Search for the term "Test Automation".
  -Verifies that the search results page contains results.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # Step 1: Open a browser and navigate to a search engine (e.g., Google)
    driver.get("https://www.google.com")

    # Step 2: Search for the term "Test Automation"
    search_box = driver.find_element(By.NAME, "q")  # Locate the search box using its name attribute
    search_box.send_keys("Test Automation")  # Enter the search term
    search_box.send_keys(Keys.RETURN)  # Simulate pressing the Enter key to search

    # Step 3: Verify that the search results page contains results
    results = driver.find_elements(By.CSS_SELECTOR, "div.g")  # Locate search results using CSS selector

    assert len(results) > 0, "No results found on the search results page."
    print("Search results are present.")

finally:
    # Step 4: Close the browser
    driver.quit()
