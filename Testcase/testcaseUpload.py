from Pages.LoginPage import *
from Pages.HomePage import *
from Pages.AppMangerPage import *
from selenium import webdriver
import unittest
from ddt import ddt,data
from common.BasePage import *

from common.ExcelUtil import ParseExcel
import common.getAllUrl
from common.getAllUrl import Get_curr_alllink
import pysnooper
from common.configRead import configRead

@ddt
class testForUpload(unittest.TestCase):
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    driver = None
    @classmethod
    def setUpClass(cls):
        print('start')
        #单例模式，保证使用同一个driver
        # if cls.driver is None :
        cls.driver = webdriver.Chrome()
        # 执行测试用例
        # dada接收方法中返回的数据，是一个列表的形式
    @pysnooper.snoop()
    def test_upload(self):
        #登录
        LoginPage(self.driver, configRead().read_username(), configRead().read_pwd()).Login()
        #主页选择项目组
        HomePage_one(self.driver).choise_project()
        #主页进入应用列表
        HomePage_one(self.driver).appmanage()
        #应用管理页面点击上传
        AppMangerPage(self.driver).upload_click()
        #上传所选择的应用
        AppMangerPage(self.driver).upload_app_byname(u"D:\\1.apk")
        sleep(5)




        sleep(3)
    @classmethod
    def tearDownClass(cls):
        print('end')
        cls.driver.quit()
        # if cls.driver:
        #     cls.driver.quit()
        # cls.driver = None


if __name__=="__main__":
    unittest.main(verbosity=2)