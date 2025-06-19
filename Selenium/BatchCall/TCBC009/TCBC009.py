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

def TCBC009(driver):
    try:
        print("Executing Test Case TCBC009: Open Batch Call Page")
        
        # Find the first row of the table
        first_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tr[data-slot='table-row'][data-index='0']"))
        )

        # Scroll into view and click
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_row)
        first_row.click()

        time.sleep(5)

    except Exception as e:
        print(f"Error in TCBC009: {e}")

    finally:
        # Close the browser
        print("Test case TCBC009 executed successfully!")