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
rows = xl.getRowCount(data, dataSheetName)
columns = xl.getColumnCount(report, reportSheetName)

colNames = {}
for col in range (1, columns):
    colName = xl.readData(report, reportSheetName, 2, col)
    colNames[colName] = col
    # colNames[col] = colName


for row in range (2, rows):
    # print("This is the row Number: " + str(row))
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
    
    rg, hol, ot, otRate, dblot, dblotRate = globals.segments(duration, brk, pabrk, payRate, shiftDate, '2024-08-08')
    otAmount = ot * otRate
    dblotAmount = dblot * dblotRate

    if hol == 0:
        payAmount = (rg * payRate) + (pabrk * payRate) + otAmount + dblotAmount
    else:
        payAmount = (hol * holRate) + (pabrk * payRate) + otAmount + dblotAmount

    row = row + 1

    lunch = xl.readData(report, reportSheetName, row, colNames['Lunch'])
    paid = xl.readData(report, reportSheetName, row, colNames['Paid Breaks'])
    hours = xl.readData(report, reportSheetName, row, colNames['Hours'])
    hoursRate = xl.readData(report, reportSheetName, row, colNames['PayRate'])
    holHours = xl.readData(report, reportSheetName, row, colNames['HOL Hours'])
    holHoursRate = xl.readData(report, reportSheetName, row, colNames['HolidayRate'])
    overtime = xl.readData(report, reportSheetName, row, colNames['OvertimeHours'])
    overtimeRate = xl.readData(report, reportSheetName, row, colNames['OTRate'])
    doubleOvertime = xl.readData(report, reportSheetName, row, colNames['DoubletimeHours'])
    doubleOvertimeRate = xl.readData(report, reportSheetName, row, colNames['DBLOTRate'])
    dollars = xl.readData(report, reportSheetName, row, colNames['Dollars'])
    holDollars = xl.readData(report, reportSheetName, row, colNames['HOLDollars'])
    otDollars = xl.readData(report, reportSheetName, row, colNames['OTDollars'])
    dblotDollars = xl.readData(report, reportSheetName, row, colNames['DBLOTDollars'])


    globals.comparission(row, brk, lunch, "non-Paid Break", "Lunch")
    globals.comparission(row, pabrk, paid, "PABRK", "Paid Break")
    globals.comparission(row, rg, hours, "Regular Hours", "Hours")
    globals.comparission(row, payRate, hoursRate, "Minimum Pay Rate", "PayRate")
    globals.comparission(row, hol, holHours, "Holiday", "Holiday Hours")
    globals.comparission(row, holRate, holHoursRate, "Holiday Pay Rate", "HolidayRate")
    globals.comparission(row, ot, overtime, "ot Hours", "OvertimeHours")
    globals.comparission(row, otRate, overtimeRate, "ot Pay Rate", "OTRate")
    globals.comparission(row, dblot, doubleOvertime, "dblot Hours", "DoubletimeHours")
    globals.comparission(row, dblotRate, doubleOvertimeRate, "dblot Pay Rate", "DBLOTRate")
    globals.comparission(row, payAmount, dollars, "Pay Amount", "Dollars")
    globals.comparission(row, otAmount, otDollars, "OT Amount", "OTDollars")
    globals.comparission(row, dblotAmount, dblotDollars, "DBLOT Amount", "DBLOTDollars")

print("All the fields in the bill side are matching correctly!!!")
driver.close()