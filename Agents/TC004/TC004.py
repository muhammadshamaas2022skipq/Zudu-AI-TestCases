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
from selenium.webdriver.common.action_chains import ActionChains

def TC_004(driver):
    try:
        print("Executing Test Case TC_004: Change Agent Voice Speed")

        Select_Speed(driver, "0.5")
        Select_Speed(driver, "1.0")
        Select_Speed(driver, "2.0")

    finally:
        # Close the browser
        print("Test case TC_004 executed successfully!")

from selenium.webdriver.common.action_chains import ActionChains

def Select_Speed(driver, speed):
    slider = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-slot='slider-thumb']"))
    )
    slider_track = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-slot='slider']"))
    )

    track_rect = slider_track.rect
    width = int(track_rect['width'])

    min_speed = 0.5
    max_speed = 2.0
    speed_float = float(speed)
    relative_pos = (speed_float - min_speed) / (max_speed - min_speed)
    target_x = int(relative_pos * width)

    # Get current slider thumb position (relative to slider left)
    thumb_rect = slider.rect
    current_x = int(thumb_rect['x'] - track_rect['x'] + thumb_rect['width'] // 2)

    move_x = target_x - current_x
    move_y = 0  # no vertical move needed

    print(f"Dragging slider thumb from {current_x}px to {target_x}px (move by {move_x}px)")

    actions = ActionChains(driver)
    actions.click_and_hold(slider).move_by_offset(move_x, move_y).release().perform()

    # Wait for value to update
    import time
    found = False
    for i in range(12):
        current_value = driver.find_element(By.CSS_SELECTOR, "[data-slot='slider-thumb'] + input").get_attribute("value")
        print(f"Waiting for speed update: attempt {i+1}, current value = {current_value}")
        try:
            if abs(float(current_value) - speed_float) < 0.11:
                found = True
                break
        except Exception as e:
            print(f"Error parsing value: {e}")
        time.sleep(0.5)

    if not found:
        print(f"Speed input value did not update to {speed_float} within expected tolerance.")

    Test_Agent(driver, f"agent_speed_{speed}.wav")

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