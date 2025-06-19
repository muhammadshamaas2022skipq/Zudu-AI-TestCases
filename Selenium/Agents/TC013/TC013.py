import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sounddevice as sd
from scipy.io.wavfile import write

def TC_013(driver):
    try:
        print("Executing Test Case TC_013: Add Knowledge Base Document")

        Add_Knowledge_Base_Document(driver, "Test Knowledge Base")

    finally:
        # Close the browser
        print("Test case TC_013 executed successfully!")

def Add_Knowledge_Base_Document(driver, document):
    # Click button to add a new document
    add_document_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add document')]"))
    )

    # Wait for overlay to disappear
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "div.w-full.flex.items-center.justify-between.shadow-lg"))
    )

    # Scroll into view (optional)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_document_button)

    # Click the button
    add_document_button.click()

    # Click the "Test Knowledge Base" button in the popover
    test_kb_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class, 'flex') and .//span[text()='"+document+"']]"
        ))
    )
    test_kb_button.click()

    time.sleep(5)
