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

def TC_009(driver):
    try:
        print("Executing Test Case TC_009: Add System Prompt Message ")

        Type_System_Prompt(driver, "Hello, I am your AI assistant. How can I help you today?")

    finally:
        # Close the browser
        print("Test case TC_009 executed successfully!")

def Type_System_Prompt(driver, message):
    # Locate the textarea for the first message
    textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "systemPrompt"))
    )

    # Clear any existing text and type the new message
    textarea.clear()
    textarea.send_keys(message)

    # Check if the message is added to the textarea
    textarea_value = textarea.get_attribute('value')
    if message in textarea_value:
        print(f"Message '{message}' added successfully to the System Prompt.")
    else:
        print(f"Failed to add message '{message}' to the System Prompt.")

    time.sleep(3)  # Wait for the message to be typed

    Test_Agent(driver, f"agent_system_prompt.wav")

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