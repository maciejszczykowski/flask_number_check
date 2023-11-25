from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Construct the path to chromedriver.exe
webdriver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver.exe')

# Initialize Chrome options and set the executable path
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"webdriver.chrome.driver={webdriver_path}")

# Initialize the Chrome driver with the specified options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to your Flask app
    driver.get("http://127.0.0.1:5000")

    # Use WebDriverWait to wait for the input field to be present.
    number_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "number"))
    )

    # Find the input field and enter "44444444"
    number_input.send_keys("44444444")

    # Find the "Check" button and click it
    check_button = driver.find_element(By.XPATH, "//button[contains(text(),'Check')]")
    check_button.click()

    # Use WebDriverWait to wait for the "Congratulations" message to be present
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Congratulations')]"))
    )

finally:
    # Close the browser window
    driver.quit()
