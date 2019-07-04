from Pages.LoginPage import *
from Pages.HomePage import *
from Pages.AppMangerPage import *
from selenium import webdriver
from common.BasePage import *
import pytest
import pysnooper
from common.configRead import configRead
import allure

class Test_DeleteApp():
    @pysnooper.snoop()
    # @pytest.mark.skpi()
    @pytest.mark.run(order=14)
    def test_Download_android(self,driver):

        #上传APP
        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        # 主页进入应用列表
        HomePage_one(driver).appmanage()
        # 应用管理页面点击上传
        AppMangerPage(driver).upload_click()
        # 上传所选择的应用
        AppMangerPage(driver).upload_app_byname(u"D:\\1.apk")
        sleep(50)
        AppMangerPage(driver).click_back_APPmanage()
        AppMangerPage(driver).click_download()
        sleep(20)


    @pytest.mark.run(order=14)
    def test_Download_android(self, driver):
        # 上传APP
        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        # 主页进入应用列表
        HomePage_one(driver).appmanage()
        # 应用管理页面点击上传
        AppMangerPage(driver).upload_click()
        # 上传所选择的应用
        AppMangerPage(driver).upload_app_byname(u"D:\\3.ipa")
        sleep(50)
        AppMangerPage(driver).click_back_APPmanage()
        AppMangerPage(driver).click_download()
        sleep(20)







