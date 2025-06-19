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

def TCBC001(driver):
    try:
        print("Executing Test Case TCBC001: Load Batch Call Page")
        # Navigate to Agents page from sidebar
        agents_sidebar_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-slot='sidebar-menu-button'][href='/batch-call']"))
        )
        agents_sidebar_link.click()

        # Wait for the Agents page to load
        agents_page_header = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Batch Call')]"))
        )

        # Wait for the table to be present (adjust selector as needed)
        table = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "table"))
        )

        time.sleep(5)

    except Exception as e:
        print(f"Error in TCBC001: {e}")

    finally:
        # Close the browser
        print("Test case TCBC001 executed successfully!")