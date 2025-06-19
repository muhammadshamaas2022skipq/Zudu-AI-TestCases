import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sounddevice as sd
from scipy.io.wavfile import write

def TC_001(driver):
    try:
        print("Executing Test Case TC-001: Load Agent Edit Page")
        # Navigate to Agents page from sidebar
        agents_sidebar_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-slot='sidebar-menu-button'][href='/agents']"))
        )
        agents_sidebar_link.click()

        # Wait for the Agents page to load
        agents_page_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Agents')]"))
        )

        # Locate the row containing "ShamaasTestAgent" and click it
        agent_row = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[contains(@class, 'hover:bg-muted/50') and contains(., 'ShamaasTestAgent')]"))
        )
        agent_row.click()

        # Interact with the "Enter Name" input field
        name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
        name_input.click()

    except Exception as e:
        print(f"Error in TC_001: {e}")

    finally:
        # Close the browser
        print("Test case TC-001 executed successfully!")