from Pages.LoginPage import *
from Pages.HomePage import *
from selenium import webdriver
import unittest
from ddt import ddt,data

from common.ExcelUtil import ParseExcel



@ddt
class testlogin(unittest.TestCase):
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    driver = None
    @classmethod
    def setUpClass(cls):
        print('start')
        #单例模式，保证使用同一个driver
        # if cls.driver is None :
        cls.driver = webdriver.Chrome()
        #执行测试用例
    @data(*excel.getDataFromSheet())
    def test_login1(self,data):


        #执行登录功能
        LoginPage(self.driver,data['username'],data['password']).Login()
        HomePage_one(self.driver).choise_project()
        HomePage_one(self.driver).appmanage()



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