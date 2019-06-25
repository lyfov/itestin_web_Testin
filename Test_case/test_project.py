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
from Pages.ManagePage import *
class Test_manageproject():

        @pytest.mark.run(orde=20)
        def test_comein_manage(self,driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()

        @pytest.mark.run(orde=21)
        def test_comein_xiangqing(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()

        @pytest.mark.run(orde=22)
        def test_manage_creat_quit(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()
            # 进入点击创建项目组
            ManagePage(driver).click_creat_project()
            ManagePage(driver).input_project_name("浩东最帅")
            #点击取消按钮
            ManagePage(driver).click_quit_creat()

        @pytest.mark.run(orde=22)
        def test_manage_creat_true(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()
            # 进入点击创建项目组
            ManagePage(driver).click_creat_project()
            ManagePage(driver).input_project_name("浩东最帅")
            #点击确认按钮
            ManagePage(driver).click_true_creat()

        @pytest.mark.run(orde=23)
        def test_manage_creat_true_emty(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()
            # 进入点击创建项目组
            ManagePage(driver).click_creat_project()
            ManagePage(driver).input_project_name("")
            # 点击确认按钮
            ManagePage(driver).click_true_creat()
            # 断言提示信息
            assert ManagePage(driver).get_text_button('//*[@id="add_project_name_msg"')=="项目组名称不能为空"

        @pytest.mark.run(orde=24)
        def test_manage_creat_true_long(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()
            # 进入点击创建项目组
            ManagePage(driver).click_creat_project()
            ManagePage(driver).input_project_name("一二三四五六七八九十一二三四五六七八九十一二三四五六七八九十")
            # 点击确认按钮
            ManagePage(driver).click_true_creat()
            # 断言提示信息
            assert ManagePage(driver).get_text_button('//*[@id="add_project_name_msg"') == "项目组名称的长度不能超过20个汉字"

        @pytest.mark.run(orde=25)
        def test_manage_creat_true_teshuzifu(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()
            # 进入点击创建项目组
            ManagePage(driver).click_creat_project()
            ManagePage(driver).input_project_name(r"!@#$%^&*()_")
            # 点击确认按钮
            ManagePage(driver).click_true_creat()

        #不输入名称
        @pytest.mark.run(orde=25)
        def test_manage_creat_true_noinput(self, driver):
            LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
            # 主页选择项目组
            HomePage_one(driver).choise_project()
            # 主页进入管理中心
            ManagePage(driver).click_comein()
            # 进入查看详情页面
            ManagePage(driver).click_chakanxiangqing_project()
            # 进入点击创建项目组
            ManagePage(driver).click_creat_project()
            # 点击确认按钮
            ManagePage(driver).click_true_creat()