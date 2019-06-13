from Pages.LoginPage import *
from Pages.HomePage import *
from Pages.AppMangerPage import *
from selenium import webdriver
from common.BasePage import *
import pytest
import pysnooper
from common.configRead import configRead
from common.ChangeHandle import *
from Pages.OnlinePage import *
class Test_RecordScript():
    @pytest.mark.skip()
    def test_RecordScript(self,driver):

        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        sleep(3)
        #点击脚本管理
        # driver=webdriver.Chrome()
        HomePage_one(driver).click_auto_script()
        HomePage_one(driver).click_recordingBtn()
        sleep(9)
    def test_Save_Empty(self,driver):

        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        sleep(3)
        #点击脚本管理
        # driver=webdriver.Chrome()
        HomePage_one(driver).click_auto_script()
        HomePage_one(driver).click_recordingBtn()
        ChangeHandle(driver).change_handle_new()
        Onlinepage(driver).click_Wait()
        ChangeHandle(driver).change_handle_old()
        sleep(9)
