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
print(rows)

for row in range (2, rows):
    # Reading the data from DB
    invDuration = xl.readData(data, dataSheetName, row, 11)
    billHrs = xl.readData(data, dataSheetName, row, 20)
    nonBillBrk = xl.readData(data, dataSheetName, row, 12) / 60
    billBrk = xl.readData(data, dataSheetName, row, 13) / 60
    billRate = xl.readData(data, dataSheetName, row, 14)
    holBillRate = (xl.readData(data, dataSheetName, row, 15) * billRate)
    otBillRate = xl.readData(data, dataSheetName, row, 21)
    dblotBillRate = xl.readData(data, dataSheetName, row, 22)
    shiftDate = xl.readData(data, dataSheetName, row, 5)
    shiftDate = str(shiftDate)
    shiftDateSplit = shiftDate.split()
    shiftDate = shiftDateSplit[0]
    rgBill, holBill, otBill, dblotBill = globals.segments(invDuration, nonBillBrk, billBrk, billRate, shiftDate, '2024-08-08')
    # print(invDuration, billHrs, billBrk, rgBill, billRate, holBill, holBillRate, otBill, otBillRate, dblotBill, dblotBillRate, shiftDate)

    row = row + 1
    # Reading the data from the Overall Report
    billableHours = xl.readData(report, reportSheetName, row, 49)
    billBreaks = xl.readData(report, reportSheetName, row, 50)
    regularBilledHours = xl.readData(report, reportSheetName, row, 51)
    billRateRep = xl.readData(report, reportSheetName, row, 52)
    holBillHours = xl.readData(report, reportSheetName, row, 53)
    holidayBillRate = xl.readData(report, reportSheetName, row, 54)
    otBilledHours = xl.readData(report, reportSheetName, row, 55)
    otBillRateRep = xl.readData(report, reportSheetName, row, 56)
    dblotBillHours = xl.readData(report, reportSheetName, row, 57)
    dblotBillRateRep = xl.readData(report, reportSheetName, row, 58)
    billableDollars = xl.readData(report, reportSheetName, row, 59)
    billableHolDollars = xl.readData(report, reportSheetName, row, 60)
    otDollars = xl.readData(report, reportSheetName, row, 61)
    dblotDollars = xl.readData(report, reportSheetName, row, 62)

    #Calculating the amounts
    otBillAmount = otBill * otBillRate
    dblotBillAmount = dblotBill * dblotBillRate

    if(holBill == 0):
        billAmount = (rgBill * billRate) + (billBrk * billRate) + otBillAmount + dblotBillAmount
    else:
        billAmount = (holBill * holBillRate) + (billBrk * billRate) + otBillAmount + dblotBillAmount
    # print(billAmount, otBillAmount, dblotBillAmount)

    globals.comparission(row, billHrs, billableHours, 'Billed Hours Data', 'Billable Hours Report')
    globals.comparission(row, billBrk, billBreaks, 'Billed Breaks Data', 'Bill Breaks report')
    globals.comparission(row, rgBill, regularBilledHours, 'Regular Billed Hours Data', 'Regular Billed Hours Report')
    globals.comparission(row, billRate, billRateRep, 'Bill Rate Data', 'Bill Rate Report')
    globals.comparission(row, holBill, holBillHours, 'Holiday Hours Data', 'Holiday Hours Report')
    globals.comparission(row, holBillRate, holidayBillRate, 'Holiday Rate Data', 'Holiday Rate Report')
    globals.comparission(row, otBill, otBilledHours, 'Overtime Data', 'Overtime Report')
    globals.comparission(row, otBillRate, otBillRateRep, 'Overtime Rate Data', 'Overtime Rate Report')
    globals.comparission(row, dblotBill, dblotBillHours, 'Double Overtime Data', 'Double Overtime Report')
    globals.comparission(row, dblotBillRate, dblotBillRateRep, 'Double Overtime Rate Data', 'Double Overtime Rate Report')
    globals.comparission(row, billAmount, billableDollars, 'Bill Amount', 'Bill Dollars')
    globals.comparission(row, holBill, billableHolDollars, 'Holidays Bill Amount', 'Holidays Bill Dollars')
    globals.comparission(row, otBillAmount, otDollars, 'Overtime Bill Amount', 'Overtime Bill Dollars')
    globals.comparission(row, dblotBillAmount, dblotDollars, 'Double Overtime Bill Amount', 'Double Overtime Bill Dollars')


print("All the fields in the bill side are matching correctly!!!")
driver.close()

