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

def TC_022(driver):
    try:
        print("Executing Test Case TC_022: Add Tool")

        Add_Tool(driver, "Transfer to Human")
        #Delete_Tool(driver, "Transfer to Human")

    finally:
        # Close the browser
        print("Test case TC_022 executed successfully!")

def Add_Tool(driver, tool):
    # Click button to add a new tool
    add_tool_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Add tool')]"))
    )
    add_tool_button.click()

    # Wait for the dropdown menu to appear and select the tool
    dropdown_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='menu']"))
    )
    # Find all menu items and select the one that matches the tool name (case-insensitive, stripped)
    menu_items = dropdown_menu.find_elements(By.XPATH, ".//div[@role='menuitem']")
    tool_option = None
    for item in menu_items:
        if item.text.strip().lower() == tool.strip().lower():
            tool_option = item
            break
    if tool_option is None:
        raise Exception(f"Could not find menu item for tool '{tool}'")
    tool_option.click()

    # Wait for the modal dialog to appear
    modal_dialog = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@role='dialog' and @data-state='open']"))
    )

    # Wait for the "Add tool" button inside the modal and click it
    add_tool_modal_button = WebDriverWait(modal_dialog, 10).until(
        EC.element_to_be_clickable((By.XPATH, ".//button[normalize-space(text())='Add tool']"))
    )
    add_tool_modal_button.click()

    time.sleep(3)

    # Verification: Check that the tool appears in the list by its name
    try:
        # The tool names in the UI use underscores instead of spaces, so convert accordingly
        tool_ui_name = tool.replace(" ", "_")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//h3[normalize-space(text())='{tool_ui_name}']"))
        )
        print(f"Tool '{tool}' was successfully added.")
    except:
        print(f"Tool '{tool}' was NOT found in the list.")

    time.sleep(3)

def Delete_Tool(driver, tool):
    try:
        # Convert tool name to match the one in the UI (e.g., "end call" → "end_call")
        tool_ui_name = tool.replace(" ", "_")

        # Locate the container for the specific tool
        tool_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                f"//h3[normalize-space(text())='{tool_ui_name}']/ancestor::div[contains(@class, 'border-')]"
            ))
        )

        # Within that container, find the trash button (second button in the list)
        trash_button = tool_container.find_elements(By.XPATH, ".//button")[1]
        trash_button.click()
        print(f"Clicked trash icon to delete '{tool}'.")

        # Optional: Wait for the tool to be removed from the DOM
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located((
                By.XPATH,
                f"//h3[normalize-space(text())='{tool_ui_name}']"
            ))
        )
        print(f"Tool '{tool}' was successfully deleted.")

    except Exception as e:
        print(f"Failed to delete tool '{tool}': {e}")






