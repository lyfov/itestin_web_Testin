import pytest
from selenium import webdriver
from Pages.LoginPage import *
from Pages.HomePage import *
from Pages.AppMangerPage import *
from common.configRead import configRead
class Test_upload():

    @pytest.fixture(scope="class")
    def driver(self):
            driver=webdriver.Chrome()
            self.driver=driver
            yield self.driver
            self.driver.close()
            return  self.driver

    def test_upload(self,driver):
        LoginPage(driver,configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        # 主页进入应用列表
        HomePage_one(driver).appmanage()
        # 应用管理页面点击上传
        AppMangerPage(driver).upload_click()
        # 上传所选择的应用
        AppMangerPage(driver).upload_app_byname(u"D:\\1.apk")
        sleep(5)