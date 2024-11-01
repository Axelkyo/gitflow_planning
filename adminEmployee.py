import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Firefox driver
service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://atzs.staffwizarddev.com")
driver.maximize_window()

driver.find_element("id", "name").send_keys("superadmin")
driver.find_element("id", "password").send_keys("s74ffw1z4rd@1234")
driver.find_element("id", "submit").click()
time.sleep(2)

driver.find_element("xpath", "//span[text()='Employees']").click()
driver.find_element("xpath", "//span[text()='Admin Staff']").click()
time.sleep(2)
driver.find_element("css selector", 'a.add-new-quiz-ek').click()
time.sleep(2)

driver.find_element("id", "f_name").send_keys("Eric")
driver.find_element("id", "l_name").send_keys("Gablehauser ")
driver.find_element("id", "searchTextField").send_keys("25020 Las Brisas Road ")
# Wait for the suggestions to appear
suggestions_list = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(("css selector", ".pac-item"))
)
# Click on the first suggestion in the list
first_suggestion = driver.find_element("css selector", ".pac-item:nth-child(1)")
first_suggestion.click()
driver.find_element("id", "phone_format").send_keys("6189999964")
dob_input = driver.find_element("id", "dob")
dob_input.send_keys("01011989")
dob_input.send_keys(Keys.TAB)
driver.find_element("name", "social_security").send_keys("999999964")

# time.sleep(5)
# driver.quit()


