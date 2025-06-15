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

def TC_002(driver):
    try:
        print("Executing Test Case TC-002: Change Agent Language")

        Select_Language(driver, "Hindi")
        Select_Language(driver, "English")
        Select_Language(driver, "Chinese")
        Select_Language(driver, "French")
        Select_Language(driver, "Japanese")

    finally:
        # Close the browser
        print("Test case TC-002 executed successfully!")

def Select_Language(driver, language):
    # Wait for the "Agent Language" dropdown button to be clickable
    agent_language_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Agent Language']/following-sibling::div//button"))
    )

    # Test Hindi language selection
    print("Changing Agent Language to "+language)

    # Click the SVG chevron (dropdown icon) inside the button
    chevron_svg = agent_language_btn.find_element(By.TAG_NAME, "svg")
    chevron_svg.click()

    # Wait for the dropdown options to be visible
    dropdown_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'absolute') and contains(@class, 'bg-white')]"))
    )

    # Wait for the language option to be present and clickable, then click it
    option = WebDriverWait(dropdown_menu, 10).until(
        EC.element_to_be_clickable((By.XPATH, f".//span[text()='{language}']"))
    )
    option.click()

    # Wait for the Save button to be clickable
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
    )

    # Wait for any toast/overlay to disappear before clicking Save
    try:
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH, "//li[@data-sonner-toast and @data-visible='true']"))
        )
    except:
        pass  # If no toast is present, continue

    save_button.click()

    Test_Agent(driver, "agent_voice_"+language+".wav")

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