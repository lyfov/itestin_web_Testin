from Pages.LoginPage import *
from Pages.HomePage import *
from Pages.AppMangerPage import *
from selenium import webdriver
from common.BasePage import *
import pytest
import pysnooper
from common.configRead import configRead
import allure

class Test_NodeApp():
    @pytest.mark.run(order=15)
    def test_nodefortest_gongneng(self, driver):
        # 上传APP
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
        #返回到应用管理
        AppMangerPage(driver).click_back_APPmanage()
        #点击功能测试记录
        AppMangerPage(driver).click_node_gongneng()


    @pytest.mark.run(order=16)
    def test_nodefortest_jianrong(self, driver):
        # 上传APP
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
        # 返回到应用管理
        AppMangerPage(driver).click_back_APPmanage()
        # 点击功能测试记录
        AppMangerPage(driver).click_node_jianrong()

    @pytest.mark.run(order=17)
    def test_nodefortest_yunjiankong(self, driver):
        # 上传APP
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
        # 返回到应用管理
        AppMangerPage(driver).click_back_APPmanage()
        # 点击功能测试记录
        AppMangerPage(driver).click_node_yunjiankong()




