from Pages.LoginPage import *
from Pages.HomePage import *
from selenium import webdriver
import unittest
from ddt import ddt,data
import pysnooper
from common.DriverChk import driverchk
from common.configRead import configRead
from common.ExcelUtil import ParseExcel
import os
@ddt
class testlogin(unittest.TestCase):
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    driver = None
    @classmethod


    def setUpClass(cls):
        print('start')
        #单例模式，保证使用同一个driver
        cls.driver =webdriver.Chrome(r'C:\Users\HP\Downloads\chromedriver_win32 (4)\chromedriver.exe')
        # cls.driver.find_element_by_class_name()
        #执行测试用例
        #dada接收方法中返回的数据，是一个列表的形式
        print(os.getcwd())
    @data(*excel.getDataFromSheet())
    @pysnooper.snoop()
    def test_login1(self,data):


        # 执行登录功能
        # data是列表，但是传参数要用里面的字典进行传递，注意，使用元组要拆分数据使用unpack修饰符

        login=LoginPage(self.driver,data['username'],data['password'])

        #输入账号密码并登录
        login.Login()
        #判断对应提示信息是否存在
        print(data['tag_message'])
        login.check_tagmessage(data['tag_message'])
        sleep(3)
    @classmethod
    def tearDownClass(cls):
        print('end')
        # driverchk.driver_quit()
        cls.driver.quit()
        # if cls.driver:
        #     cls.driver.quit()
        # cls.driver = None


if __name__=="__main__":
    unittest.main(verbosity=2)