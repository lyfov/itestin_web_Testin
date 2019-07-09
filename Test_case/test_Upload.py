import pytest

from Pages.AppMangerPage import *
from Pages.HomePage import *
from Pages.LoginPage import *
from common.configRead import configRead


class Test_upload():
    # @pytest.mark.skip()
    # @pytest.mark.run(order=1)
    def test_upload_adnroid(self,driver):
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

    # @pytest.mark.skip()
    @pytest.mark.run(order=13)
    def test_upload_ios(self, driver):
        LoginPage(driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(driver).choise_project()
        # 主页进入应用列表
        HomePage_one(driver).appmanage()
        # 应用管理页面点击上传
        AppMangerPage(driver).upload_click()
        # 上传所选择的应用
        AppMangerPage(driver).upload_app_byname(u"D:\\3.ipa")
        sleep(5)