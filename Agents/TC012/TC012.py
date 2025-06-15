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

def TC_012(driver):
    try:
        print("Executing Test Case TC_012: Enable/Disable Webhook Toggle ")

        Enable_Webhook_Toggle(driver)

    finally:
        # Close the browser
        print("Test case TC_012 executed successfully!")

def Enable_Webhook_Toggle(driver):
    # Find the toggle button using its unique attributes and click it
    toggle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[role='switch'][data-slot='switch']"))
    )
    toggle_button.click()

    # Wait for the Save button to be present
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Save']"))
    )

    # Wait for any toast/overlay to disappear before clicking Save
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, "li[data-sonner-toast][data-visible='true']"))
    )

    # Now wait for the Save button to be clickable and click it
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
    )
    save_button.click()

    time.sleep(5)

    # Verify that the toggle button is still enabled (checked)
    toggle_state = toggle_button.get_attribute("aria-checked")
    assert toggle_state == "true", "Toggle button is not enabled after saving."
    print("Toggle button is still enabled after saving.")
