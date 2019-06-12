from Pages.LoginPage import *
from Pages.HomePage import *
from Pages.AppMangerPage import *
from selenium import webdriver
from common.BasePage import *
import pytest
import pysnooper
from common.configRead import configRead

class Test_DeleteApp():
    @pytest.fixture(scope="class")
    def driver(self):
        print("========================================")
        self.driver = webdriver.Chrome()
        yield self.driver
        self.driver.close()
        return self.driver
    @pysnooper.snoop()
    def test_Deleteapp(self,driver):
        #登录
        print(driver)
        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        #主页选择项目组
        HomePage_one(driver).choise_project()
        #主页进入应用列表
        HomePage_one(driver).appmanage()
        #应用管理页面查找应用
        AppMangerPage(driver).selectByAppName("涨乐财富通")
        #9
        AppMangerPage(driver).DeleteApp("涨乐财富通")
        #断言是否删除成功
        assert AppMangerPage(self.driver).Get_Alert_message()=="删除成功"