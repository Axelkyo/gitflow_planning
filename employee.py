import time
import os
from dotenv import load_dotenv
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
        element.send_keys(key)
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

# oppening the Staffwizard site on ATZS instance
driver.get("https://atzs.staffwizard.com")
driver.maximize_window()
time.sleep(3)

# Login as superadmin
driver.find_element("id", "name").send_keys(os.getenv('USER'))
driver.find_element("id", "password").send_keys(os.getenv('PASS'))
driver.find_element("id", "submit").click()

# Navigating to Add New Employee
type_click("employee",5,"xpath","//span[text()='Employees']")
type_click("available", 5, "xpath", "//span[contains(text(),'Available Employees')]")
type_click("addNew", 5, "xpath", "//a[contains(.,'Add New')]")

# Filling the forms
type_text("fname", 5, "id", "f_name", "Freezing2")
type_text("lname", 5, "id", "l_name", "Adding2")
type_text("address", 5, "id", "searchTextField", "Main Street Bellevue, 98004")
type_click("suggested", 5, "css selector", ".pac-item:nth-child(1)")
type_text("mobile", 5, "id", "phone_format", "6189999955")
type_text("email", 5, "id", "p_email", "atzael+freezing@staffwizard.com")

dob = type_text("dob", 5, "id", "dob", "01-01-1989")
dob.send_keys(Keys.TAB)

type_text("ssn", 5, "css selector", "input[name='social_security']", "999999955")
type_select("region", 5, "id", "master_region_id", "3")
time.sleep(2)
type_select("branch", 5, "id", "branch", "61")
type_select("status", 5, "id", "status", "1")

hireDate = type_text("hireDate", 5, "name", "hire_date", "01-01-2022")
hireDate.send_keys(Keys.TAB)

joinDate = type_text("joinDate", 5, "name", "joining_date", "01-03-2022")
joinDate.send_keys(Keys.TAB)

type_click("submit", 5, "name", "submit1")

view_confirmation("newEmp", 10, "xpath", "//a[contains(.,'Freezing')]").click()

time.sleep(2)