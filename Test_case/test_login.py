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
    proDir = os.path.split(os.path.realpath(__file__))[0]
    proDir=proDir+r"/1.xlsx"
    print(proDir)
    excel = ParseExcel(proDir, "Sheet1")
    @pytest.mark.parametrize("username,password,tag_message",excel.getDataFromSheet())
    # @pytest.mark.skpi()
    @pytest.mark.run(order=3)
    def test_login(self,driver,username,password,tag_message):
        print(username)
        # print(data['username'])
        login = LoginPage(driver, username, password)
        login.Login()
        print(tag_message)
        login.check_tagmessage(tag_message)
        sleep(3)


