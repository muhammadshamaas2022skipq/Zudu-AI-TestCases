# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

class TestKnowledgebasepage():
  def __init__(self, driver):
    self.driver = driver
    self.vars = {}

  def setup_method(self, method):
    pass  

  def teardown_method(self, method):
    pass
  
  def test_knowledgebasepage(self):
    self.driver.get("https://app.uat.zudu.ai/")
    self.driver.set_window_size(1300, 736)
    self.driver.execute_script("document.body.style.zoom='0.5'")

    def click_element(by, value, sleep_time=1):
        from selenium.common.exceptions import TimeoutException
        try:
          element = WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable((by, value))
          )
          self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
          if element and element.is_displayed() and element.is_enabled():
            size = element.size
            if size['width'] > 0 and size['height'] > 0:
              print(element)
              try:
                element.click()
              except Exception as e:
                print(f"Click intercepted, trying JS click: {e}")
                #self.driver.execute_script("arguments[0].click();", element)
            else:
              print(f"Element found but has zero size: {element}")
          else:
            print(f"Element found but not interactable: {element}")
          time.sleep(5)
        except TimeoutException:
          print(f"Timeout: Element by {by} with value '{value}' not clickable after waiting.")
        except Exception as e:
          print(f'Error finding or clicking element by {by} with value "{value}": {e}')

    def send_keys(by,value,keys):
      try:
          input_elem = WebDriverWait(self.driver, 10).until(
              EC.element_to_be_clickable((by, value))
          )
          input_elem.send_keys(keys)
      except Exception as e:
          print(f"Could not find or interact with input: {e}")
  
    click_element(By.CSS_SELECTOR, "li:nth-child(5) span")

    # Search
    click_element(By.CSS_SELECTOR, ".file\\3Atext-foreground")
    send_keys(By.CSS_SELECTOR, ".file\\3Atext-foreground","Knowledge base")

    # Create knowledge base
    click_element(By.XPATH, "//button[normalize-space()='Create Knowledge Base']")

    time.sleep(5)

    # Name
    click_element(By.ID, "kb-name")
    send_keys(By.ID, "kb-name", "Test KB")

    # Document
    # Upload CSV file using the file input
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "recipients-template.csv"))
    file_input = WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    self.driver.execute_script("arguments[0].classList.remove('hidden');", file_input)
    file_input.send_keys(csv_path)
    time.sleep(2)

    # Text
    click_element(By.CSS_SELECTOR, ".bg-gray-50:nth-child(2)")
    click_element(By.ID, "text-title")
    send_keys(By.ID, "text-title", "Test")
    click_element(By.ID, "text-content")
    send_keys(By.ID, "text-content", "Test content")
    click_element(By.CSS_SELECTOR, ".inline-flex:nth-child(3)")

    # URL
    click_element(By.CSS_SELECTOR, ".bg-gray-50:nth-child(3)")    
    click_element(By.ID, "url-input")
    send_keys(By.ID, "url-input", "https://www.abc.com")
    click_element(By.CSS_SELECTOR, ".bg-background:nth-child(2)")

    # Save
    click_element(By.CSS_SELECTOR, ".flex-col-reverse > .bg-black")
    click_element(By.XPATH, "//td[normalize-space()='Test knowledge base']")

    # Preview
    click_element(By.CSS_SELECTOR, ".whitespace-pre-wrap")
    click_element(By.CSS_SELECTOR, ".disabled\\3Apointer-events-none:nth-child(2)")    
    click_element(By.CSS_SELECTOR, ".inline-flex:nth-child(3)")
