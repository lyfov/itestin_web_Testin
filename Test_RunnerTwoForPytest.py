
import unittest
import HTMLTestRunner
import os
from Test_case.testForLogin import *
from Test_case.testddt import *
from Test_case.testcaseUpload import *
from Test_case.Test_DeleteAPP import testDeleteApp
import time
class RunnerForTestin():

    def test_home(self):
        # 登录
        LoginPage(self.driver, configRead().read_username(), configRead().read_pwd()).Login()
        # 主页选择项目组
        HomePage_one(self.driver).choise_project()
        # 主页进入应用列表
        HomePage_one(self.driver).appmanage()
        # 应用管理页面点击上传
        AppMangerPage(self.driver).upload_click()
        # 上传所选择的应用
        AppMangerPage(self.driver).upload_app_byname(u"D:\\1.apk")
        sleep(5)


