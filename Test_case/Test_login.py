from Pages.LoginPage import *
from Pages.HomePage import *
import pysnooper
from common.DriverChk import driverchk
from common.configRead import configRead
from common.ExcelUtil import ParseExcel
import pytest
import allure


import os
class Test_ForLogin():
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    @pytest.mark.parametrize("username,password,tag_message",excel.getDataFromSheet())
    # @pytest.mark.skpi()
    def test_login(self,driver,username,password,tag_message):
        print(username)
        # print(data['username'])
        login = LoginPage(driver, username, password)
        login.Login()
        print(tag_message)
        login.check_tagmessage(tag_message)
        sleep(3)


