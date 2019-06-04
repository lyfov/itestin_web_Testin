from Pages.LoginPage import *
from Pages.HomePage import *
from selenium import webdriver
import unittest
from ddt import ddt,data
import pysnooper
from common.DriverChk import driverchk
from common.configRead import configRead
from common.ExcelUtil import ParseExcel
import pytest
from selenium import webdriver

import os
class Test_ForLogin():
    @pytest.fixture(scope="class")
    def driver(self):
        driver=webdriver.Chrome()
        self.driver=driver
        yield self.driver
        self.driver.close()
        return  self.driver
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    @pytest.mark.parametrize("username,password,tag_message",excel.getDataFromSheet())
    def test_login(self,username,password,tag_message,driver):
        print(username)
        # print(data['username'])
        login = LoginPage(driver, username, password)
        login.Login()
        print(tag_message)
        login.check_tagmessage(tag_message)
        sleep(3)


