from browserbase import Browserbase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.remote_connection import RemoteConnection
import time
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from test_signin import TestSignin
from test_agentspage import TestAgentspage
from test_callhistorypage import TestCallhistorypage
from test_batchcallpage import TestBatchcallpage

load_dotenv()

# Setup Browserbase
bb = Browserbase(api_key=os.getenv("API_KEY"))
session = bb.sessions.create(project_id=os.getenv("PROJECT_ID"))

# Custom connection with auth
class AuthConnection(RemoteConnection):
    def __init__(self, remote_url, signing_key):
        super().__init__(remote_url, keep_alive=True)
        self._signing_key = signing_key

    def get_remote_connection_headers(self, parsed_url, keep_alive=False):
        headers = super().get_remote_connection_headers(parsed_url, keep_alive)
        headers.update({"x-bb-signing-key": self._signing_key})
        return headers

conn = AuthConnection(session.selenium_remote_url, session.signing_key)

# Set Chrome options
chrome_options = Options()

# Start browser
driver = webdriver.Remote(command_executor=conn, options=chrome_options)

driver.set_window_size(1300, 736)
driver.execute_script("document.body.style.zoom='0.5'")

# Create an instance of TestSignin and call test_signin, passing driver as an argument
test_signin_instance = TestSignin(driver)
test_signin_instance.test_signin()
time.sleep(3)

# Create an instance of TestAgentspage and call test_agentspage, passing driver as an argument
test_agents_instance = TestAgentspage(driver)
test_agents_instance.test_agentspage()
time.sleep(3)

# Create an instance of TestCallhistorypage and call test_signin, passing driver as an argument
test_call_history_instance = TestCallhistorypage(driver)
test_call_history_instance.test_callhistorypage()
time.sleep(3)

# Create an instance of TestCallhistorypage and call test_signin, passing driver as an argument
test_batch_call_instance = TestBatchcallpage(driver)
test_batch_call_instance.test_batchcallpage()
time.sleep(3)

# Done
driver.quit()
