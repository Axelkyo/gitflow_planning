from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from features.functions.commands import globals
from features.functions.excel import *

service = Service(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)
globals = globals(driver)
xl = funxl(driver)

report = "E://Mis Carpetas//Advante Digital//StaffWizard//Selenium Automation//Staffwizard Automation//features//xlsx//Overall Report.xlsx"
data = "E://Mis Carpetas//Advante Digital//StaffWizard//Selenium Automation//Staffwizard Automation//features//xlsx//Overall Data.xlsx"
reportSheetName = "Overall Report"
dataSheetName = "Overall Data"
rowsReport = xl.getRowCount(report, reportSheetName)
rowsData = xl.getRowCount(data, dataSheetName)
columns = xl.getColumnCount(report, reportSheetName)
print(rowsReport)
print(rowsData)

colReport = {}
for col in range (1, columns):
    colName = xl.readData(report, reportSheetName, 2, col)
    colReport[colName] = col
    # colReport[col] = colName
print(colReport)

colData = {}
for col in range (1, columns):
    colName = xl.readData(data, dataSheetName, 2, col)
    colData[colName] = col
    # colData[col] = colName
print(colData)

employeesData = {}
for row in range(3, rowsData):
    rowName = xl.readData(data, dataSheetName, row, 3)
    employeesData[row] = rowName

employeesReport = {}
for row in range(3, rowsReport):
    rowName = xl.readData(report, reportSheetName, row, 24)
    employeesReport[row] = rowName

row = 3

firstName = xl.readData(data, dataSheetName, row, 3)
lastName = xl.readData(data, dataSheetName, row, 4)
shiftDate = xl.readData(data, dataSheetName, row, 5)

shiftDate = str(shiftDate)
shiftDateSplit = shiftDate.split()
shiftDate = shiftDateSplit[0]

duration = xl.readData(data, dataSheetName, row, 6)
brk = xl.readData(data, dataSheetName, row, 7) / 60
pabrk = xl.readData(data, dataSheetName, row, 8) / 60
payRate = xl.readData(data, dataSheetName, row, 9)
holRate = (xl.readData(data, dataSheetName, row, 10) * payRate)
