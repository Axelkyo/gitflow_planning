from behave import *
from sys import executable
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


@given(u'Lunch Time')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Lunch Time')


@when(u'Paid Breaks')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Paid Breaks')


@when(u'Hours')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Hours')


@when(u'Pay Rate')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Pay Rate')


@when(u'Hol Hours')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Hol Hours')


@when(u'Hol Rate')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Hol Rate')


@when(u'OT Hours')
def step_impl(context):
    raise NotImplementedError(u'STEP: When OT Hours')


@when(u'OT Rate')
def step_impl(context):
    raise NotImplementedError(u'STEP: When OT Rate')


@when(u'DBLOT Hours')
def step_impl(context):
    raise NotImplementedError(u'STEP: When DBLOT Hours')


@when(u'DBLOT Rate')
def step_impl(context):
    raise NotImplementedError(u'STEP: When DBLOT Rate')


@when(u'Dollars')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Dollars')


@when(u'Hol Dollars')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Hol Dollars')


@when(u'OT Dollars')
def step_impl(context):
    raise NotImplementedError(u'STEP: When OT Dollars')


@then(u'DBLOT Dollars')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then DBLOT Dollars')