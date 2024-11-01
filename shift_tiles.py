import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from features.functions.commands import globals
from features.functions.excel import *

service = Service(executable_path = GeckoDriverManager().install())
driver = webdriver.Firefox(service = service)
globals = globals(driver)
xl = funxl(driver)

dataXL = "E://Mis Carpetas//Advante Digital//StaffWizard//Selenium Automation//Staffwizard Automation//features//xlsx//query_data.xlsx"
sheetName = "query"
rows = xl.getRowCount(dataXL, sheetName)
print(rows, type(rows))

for row in range(1, rows):
    shiftID = xl.readData(dataXL, sheetName, row + 1, 1)
    shiftDate = xl.readData(dataXL, sheetName, row + 1, 4)
    shiftDate = str(shiftDate)
    shiftDateSplit = shiftDate.split()
    shiftDate = shiftDateSplit[0]
    # print(shiftID,type(shiftID), shiftDate)

    # Open and read the JSON file
    with open('features/json/date.json', 'r') as json_file:
        dataJson = json.load(json_file)

    # Extract the values from the shift
    jsonID = int(dataJson['shifts'][row - 1]['id'])
    oldEndDate = dataJson['shifts'][row - 1]['shift_end_date_time']
    oldEndDate = str(oldEndDate)
    oldEndDateSplit = oldEndDate.split()
    oldEndDate = oldEndDateSplit[0]
    correctDate = dataJson['shifts'][row - 1]['correct_end_date']
    # print(jsonID,type(jsonID), correctDate)

    if(shiftID == jsonID):
        if(shiftDate == correctDate):
            print("For the shiftID = {} the date was corrected successfully from: {} to: {}".format(shiftID, oldEndDate, correctDate))
            xl.writeData(dataXL, sheetName, row + 1, 6, 'PASSED')
        else:
            print("The date wasn't be corrected")
            xl.writeData(dataXL, sheetName, row + 1, 6, 'FAILED')
    else:
        print("The IDs from json and excel are not matching")
        xl.writeData(dataXL, sheetName, row + 1, 6, 'FAILED')

driver.close()






