from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class globals():

    def __init__(self, driver):
        self.driver = driver

    def openBrowser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def segments(self, duration, brk, pabrk, payRate, shiftDate, holDate):
        otRate = payRate * 1.5
        dblotRate = payRate * 2.0
        if(duration <= 8):
            rg = duration - (brk + pabrk)
            ot = 0
            dblot = 0
            if(shiftDate == holDate):
                hol = rg
                rg = 0
            else:
                hol = 0
            if(shiftDate == '2024-08-10' or shiftDate == '2024-08-11'):
                ot = rg
                rg = 0
            return rg, hol, ot, otRate, dblot, dblotRate
            # return rg, hol, ot, dblot
        elif(duration > 8 and duration <= 12):
            rg = 8
            ot = duration - (rg + brk + pabrk)
            dblot = 0
            if (shiftDate == holDate):
                hol = rg
                rg = 0
            else:
                hol = 0
            if (shiftDate == '2024-08-10'):
                ot = rg + ot
                rg = 0
            if(shiftDate == '2024-08-11'):
                dblot = ot
                ot = rg
                rg = 0
            return rg, hol, ot, otRate, dblot, dblotRate
            # return rg, hol, ot, dblot
        elif(duration > 12):
            rg = 8
            ot = 4
            dblot = duration - (rg + ot + brk + pabrk)
            if (shiftDate == holDate):
                hol = rg
                rg = 0
            else:
                hol = 0
            if (shiftDate == '2024-08-10'):
                ot = rg + ot
                rg = 0
            if (shiftDate == '2024-08-11'):
                dblot = ot + dblot
                ot = rg
                rg = 0
        return rg, hol, ot, otRate, dblot, dblotRate
        # return rg, hol, ot, dblot

    def comparission(self, row, dataField, repField, dataTypeField, repTypeField):
        if(dataField != repField):
            if((dataField - float(repField)) > 0.1):
                print("The row #{} has issues!!!!".format(row))
                print("The {} field and {} field are NOT matching".format(dataTypeField, repTypeField))
                print("The {} is: ".format(dataTypeField) + str(dataField))
                print("The {} is: ".format(repTypeField) + str(repField))
                print("The difference is: " + str(dataField - repField))
                print("")
            # else:
            #     print("Rounding Issues")
        # else:
            # print(repField, dataField, dataTypeField, repTypeField)
