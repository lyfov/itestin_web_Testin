from common.configRead import configRead
from selenium import webdriver
class driverchk():

    def __init__(self):
        return driverchk
    def driverchk(self):
        if configRead.read_driver() =="webdriver.Chrome()":
            self.driver =webdriver.Chrome()
        return self.driver
    def driver_quit(self):
        if configRead.read_driver() =="webdriver.Chrome()":
            self.driver =webdriver.Chrome()
            self.driver.quit()
if __name__=="__main__":
    print(driverchk.driverchk())