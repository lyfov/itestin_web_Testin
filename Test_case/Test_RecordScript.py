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

    @pytest.mark.skip()
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

    def test_Creat_Script(self, driver):
        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        sleep(3)
        # 点击脚本管理
        # driver=webdriver.Chrome()
        HomePage_one(driver).click_auto_script()
        #点击录制按钮
        HomePage_one(driver).click_recordingBtn()
        #切换到新的handle
        ChangeHandle(driver).change_handle_new()
        #点击上方等待按钮
        Onlinepage(driver).click_Wait()
        #点击等待下拉框中的等待
        Onlinepage(driver).click_WaitForWait()
        #点击确认
        Onlinepage(driver).click_Makesure()
        #点击保存
        sleep(3)
        Onlinepage(driver).click_Save()
        sleep(9)
        #点击一个单选框
        Onlinepage(driver).click_app_choose()
        sleep(3)
        #点击确定按钮
        Onlinepage(driver).click_app_sure()
        #输入脚本名称
        Onlinepage(driver).input_script_text("创建一个小脚本")
        #点击确定按钮
        Onlinepage(driver).click_script_Makesure()
        #点击更新描述的保存按钮
        Onlinepage(driver).click_updata_Makesure()
