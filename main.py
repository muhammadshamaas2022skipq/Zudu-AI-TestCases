import time
import sounddevice as sd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scipy.io.wavfile import write

# Use WebDriverManager to handle ChromeDriver installation and path
service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

# Import your test cases
from Agents.TC001.TC001 import TC_001
from Agents.TC002.TC002 import TC_002
from Agents.TC003.TC003 import TC_003
from Agents.TC004.TC004 import TC_004

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Open the URL
    driver.get("https://app.uat.zudu.ai")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Maximize the browser window
    driver.maximize_window()
    time.sleep(2)  # Wait for the window to maximize

    # Wait for the email input field to be present and interactable
    email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("admin@example.com")

    # Enter password
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("admin123")

    # Click the Sign In button
    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'][class*='inline-flex'][class*='bg-black']"))
    )
    sign_in_button.click()

    # Wait for the dashboard to load
    dashboard_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-slot='sidebar-menu-button'][href='/']"))
    )
    dashboard_link.click()

    # Run the test cases
    TC_001(driver)
    TC_002(driver)
    TC_003(driver)
    TC_004(driver)

finally:
    # Close the browser
    driver.quit()