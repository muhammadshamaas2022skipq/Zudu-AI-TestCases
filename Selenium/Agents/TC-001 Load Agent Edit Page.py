import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Use WebDriverManager to handle ChromeDriver installation and path
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sounddevice as sd
from scipy.io.wavfile import write

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

    # Wait for the page to load completely
    #page_loaded = WebDriverWait(driver, 20).until(
    #    EC.presence_of_element_located((By.CSS_SELECTOR, "form.relative.md\\:max-w-[728px]"))
    #)

    # Interact with the "Enter Name" input field
    name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
    name_input.click()

    # Interact with the "Test AI agent" button
    test_ai_agent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-slot='button']"))
    )
    test_ai_agent_button.click()

    # Record audio for 10 seconds
    duration = 10  # seconds
    sample_rate = 44100  # Hz
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save the recorded audio to a file
    output_file = "agent_voice.wav"
    write(output_file, sample_rate, audio_data)
    print(f"Audio saved to {output_file}")

    print("Test case executed successfully!")

finally:
    # Close the browser
    driver.quit()