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
class testDeleteApp(unittest.TestCase):
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
        #应用管理页面查找应用
        AppMangerPage(self.driver).selectByAppName("涨乐财富通")
        #删除应用
        AppMangerPage(self.driver).DeleteApp("涨乐财富通")
        #断言是否删除成功
        self.assertEqual(AppMangerPage(self.driver).Get_Alert_message(),"删除成功","删除失败了~~~~~~~~~~")





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