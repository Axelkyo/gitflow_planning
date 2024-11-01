import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# Initialize the Chrome driver
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

# Function for text fields
def type_text(element, timeout, selector, value, key):
    try:
        element = (
            WebDriverWait(driver, timeout)
            .until(EC.visibility_of_element_located((selector, value))))
        element.send_keys(Keys.DELETE + key)
        return element
    except TimeoutException as ex:
        print(ex.msg)
        print("Never Found The Element")

# Function for clickable elements
def type_click(element, timeout, selector, value):
    try:
        element = (
            WebDriverWait(driver, timeout)
            .until(EC.visibility_of_element_located((selector, value))))
        element.click()
        return element
    except TimeoutException as ex:
        print(ex.msg)
        print("Never Found The Element")

# Function for select fields
def type_select(element, timeout, selector, value, selection):
    try:
        element = Select(
            WebDriverWait(driver, timeout)
            .until(EC.visibility_of_element_located((selector, value))))
        element.select_by_value(selection)
        return element
    except TimeoutException as ex:
        print(ex.msg)
        print("Never Found The Element")

# Function for validate the visibility of an element
def view_confirmation(element, timeout, selector, value):
    try:
        element = (
            WebDriverWait(driver, timeout)
            .until(EC.visibility_of_element_located((selector, value))))
        return element
    except TimeoutException as ex:
        print(ex.msg)
        print("Never Found The Element")

def type_link(element, selector, value):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((selector, value)))
        element.click()
    except TimeoutException as ex:
        print(ex.msg)
        print("Never found the element")

# oppening the Staffwizard site on ATZS instance
driver.get("https://atzs.staffwizard.com")
driver.maximize_window()
time.sleep(1)

# Login as superadmin
driver.find_element("id", "name").send_keys("superadmin")
driver.find_element("id", "password").send_keys("s74ffw1z4rd@1234")
driver.find_element("id", "submit").click()

# Navigating into Timeslips module
type_link("timeslips", "link text", "Timeslip")

# Deleting the works start date field
start = view_confirmation("timeslip", 5, "name", "work_start_date")
start.send_keys(Keys.DELETE + Keys.TAB + Keys.DELETE + Keys.ENTER)
type_click("new", 5, "class name", "addTimeslip")
type_click("client", 5, "id", "select2-customer_id-container")
clientResults = type_text("clientResults", 5, "class name", "select2-search__field", "The Orange Conty")
clientResults.send_keys(Keys.ENTER)
type_click("post", 5, "id", "select2-post_location_name-container")
postResults = type_text("postResults", 5, "class name", "select2-search__field", "New Port")
postResults.send_keys(Keys.ENTER)
type_click("emp", 5, "id", "select2-employee_id-container")
empResults = type_text("empResults", 5, "class name", "select2-search__field", "Marissa")
empResults.send_keys(Keys.ENTER)
batch = type_text("batch", 5, "id", "batch_date", "08312024")
batch.send_keys(Keys.ENTER)
start = type_text("start", 5, "id", "work_start_date", "08192024")
start.send_keys(Keys.ENTER)
end = type_text("end", 5, "id", "work_end_date", "08262024")
end.send_keys(Keys.ENTER)
type_text("payHours", 5, "id", "regular_pay_hrs", "40.00")
type_text("otHours", 5, "id", "ovt_pay_hrs", "5.00")
type_text("dblotHours", 5, "id", "dbl_pay_hrs", "5.00")
time.sleep(1)
type_select("freq", 5, "id", "pay_frequency", "Weekly")
type_click("addTimeslip", 5, "css selector", "input[value='Close & Add TimeSlip']")

time.sleep(2)
