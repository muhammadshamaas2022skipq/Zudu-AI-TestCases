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

def TC_015(driver):
    try:
        print("Executing Test Case TC_015: Add Knowledge Base Document")

        Add_Knowledge_Base_Document(driver, "Add Files")

    finally:
        # Close the browser
        print("Test case TC_015 executed successfully!")

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

    # Wait for the popover to be visible
    popover = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='dialog'][data-slot='popover-content']"))
    )

    # Try to find the Add Files button
    try:
        # Wait until the button is clickable
        add_files_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[normalize-space(text())='Add Files']]"))
        )

        # Wait for overlays to disappear (adjust selector as needed)
        try:
            WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, ".your-overlay-class"))
            )
        except:
            pass  # If overlay not found, continue

        # Scroll into view
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_files_button)

        # Try normal click, fallback to JS click if intercepted
        try:
            add_files_button.click()
        except Exception as e:
            driver.execute_script("arguments[0].click();", add_files_button)
    except Exception as e:
        buttons = popover.find_elements(By.TAG_NAME, "button")
        raise e

    time.sleep(5)

    # 1. Wait for the dialog to be visible
    dialog = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div[role='dialog'][data-slot='dialog-content']"))
    )

    # Wait for the input to appear inside the dialog
    kb_name_input = WebDriverWait(dialog, 10).until(
        EC.visibility_of_element_located((By.ID, "kb-name"))
    )
    kb_name_input.clear()
    kb_name_input.send_keys("Test Knowledge Base")

    buttons = dialog.find_elements(By.TAG_NAME, "button")
    
    # Find all buttons in the dialog
    for btn in buttons:
        if btn.text.strip() == "Text (0)":
            try:
                btn.click()
            except Exception:
                driver.execute_script("arguments[0].click();", btn)
            break
    else:
        raise Exception("Text (0) button not found in dialog")

    # Wait for the Title input to appear and fill it
    title_input = WebDriverWait(dialog, 10).until(
        EC.visibility_of_element_located((By.ID, "text-title"))
    )
    title_input.clear()
    title_input.send_keys("Sample Title")

    # Wait for the Content textarea to appear and fill it
    content_textarea = WebDriverWait(dialog, 10).until(
        EC.visibility_of_element_located((By.ID, "text-content"))
    )
    content_textarea.clear()
    content_textarea.send_keys("Sample content for the knowledge base.")

    # Click the 'Add Text Source' button
    add_text_source_button = WebDriverWait(dialog, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[.//text()[normalize-space()='Add Text Source']]") )
    )
    add_text_source_button.click()

    # Click the 'Create Knowledge Base' button
    create_kb_button = WebDriverWait(dialog, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[.//text()[normalize-space()='Create Knowledge Base']]") )
    )
    create_kb_button.click()

    time.sleep(5)
