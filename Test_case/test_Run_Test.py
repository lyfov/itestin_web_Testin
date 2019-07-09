import pytest

from Pages.HomePage import *
from Pages.LoginPage import *
from Pages.StartTestPage import *
from common.BasePage import *
from common.configRead import configRead


class Test_Run_Test():
    #测试功能自动化测试列表的进入
    # @pytest.mark.skip()
    @pytest.mark.run(order=7)
    def test_Run_ComeTO_Testforgn(self, driver):
        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # HomePage_one(driver).click_TestManage()
        #点击自动化功能测试按钮，进入功能测试列表
        HomePage_one(driver).click_gongneng()

    @pytest.mark.run(order=8)
    def test_Run_Test(self, driver):
        #点击开始测试按钮
        StartTestPage(driver).click_StartTest_button()
        #选择应用
        StartTestPage(driver).choose_app_wuxianji()
        #点击下一步
        StartTestPage(driver).click_next_step()
        #添加脚本
        StartTestPage(driver).add_script()
        print("添加脚本成功")
        #点击下一步
        StartTestPage(driver).click_next_step()
        print("下一步点击成功")
        sleep(3)
        #添加全部设备
        StartTestPage(driver).add_devices_all()
        #点击下一步
        sleep(10)
        StartTestPage(driver).click_device_next()
        #输入任务名称
        StartTestPage(driver).input_test_name("测试任务")
        #点击提交测试
        StartTestPage(driver).click_subtest()
        # 点击查看任务按钮
        StartTestPage(driver).click_check_task()

    def test_Run_Test_timing(self, driver):
        #点击定时任务
        HomePage_one(driver).click_dingshirenwu()
