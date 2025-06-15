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

def TC_010(driver):
    try:
        print("Executing Test Case TC_010: Add System Variable to System Prompt ")

        Add_System_Prompt_System_Variable(driver, "system__call_sid")

    finally:
        # Close the browser
        print("Test case TC_010 executed successfully!")

def Add_System_Prompt_System_Variable(driver, variable):
    # Locate the textarea for the System Prompt
    textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "systemPrompt"))
    )

    # Scroll to the textarea and ensure it's visible
    driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
    time.sleep(1)

    # Click to focus the textarea (if needed)
    textarea.click()
    add_variable_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Add Variable'])[2]"))
    )
    add_variable_button.click()

    # Select the "system__agent_id" from the dropdown
    system_agent_id_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//p[text()='"+variable+"']]"))
    )
    system_agent_id_button.click()

    # Check if the variable is added to the textarea
    textarea_value = textarea.get_attribute('value')
    if variable in textarea_value:
        print(f"Variable '{variable}' added successfully to the System Prompt.")
    else:
        print(f"Failed to add variable '{variable}' to the System Prompt.")

    time.sleep(5)

    Test_Agent(driver, f"agent_system_prompt_system_variable_{variable}.wav")

def Test_Agent(driver, filename):
    # Interact with the "Test AI agent" button
    test_ai_agent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-slot='button']"))
    )
    test_ai_agent_button.click()

    # Record audio for 10 seconds
    duration = 3  # seconds
    sample_rate = 44100  # Hz
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save the recorded audio to a file
    output_file = filename
    write(output_file, sample_rate, audio_data)
    print(f"Audio saved to {output_file}")
    
    # Click the "End call" button
    end_call_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='End call']]"))
    )
    end_call_button.click()