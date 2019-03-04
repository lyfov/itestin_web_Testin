from Pages.LoginPage import *
from Pages.HomePage import *
from selenium import webdriver
import unittest

class testlogin(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        print('start')
        #单例模式，保证使用同一个driver
        # if cls.driver is None:
        cls.driver = webdriver.Chrome()
        #执行测试用例
    def test_login1(self):
        #执行登录功能
        LoginPage(self.driver).Login()
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