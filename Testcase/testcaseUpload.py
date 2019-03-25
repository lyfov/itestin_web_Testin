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



@ddt
class testlogin2(unittest.TestCase):
    excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx", "Sheet1")
    driver = None
    @classmethod
    def setUpClass(cls):
        print('start')
        #单例模式，保证使用同一个driver
        # if cls.driver is None :
        cls.driver = webdriver.Chrome()
        #执行测试用例
        #dada接收方法中返回的数据，是一个列表的形式
    # @data(*excel.getDataFromSheet())
    # def test_upload(self,data):
    #
    #
    #     # 执行登录功能
    #     # data是列表，但是传参数要用里面的字典进行传递，注意，使用元组要拆分数据使用unpack修饰符
    #     LoginPage(self.driver,data['username'],data['password']).Login()
    #     HomePage_one(self.driver).choise_project()
    #     HomePage_one(self.driver).appmanage()
    #     AppMangerPage(self.driver).upload_click()
    #     AppMangerPage(self.driver).upload_app_byname(u"D:\\迅雷下载\\82bbe3c6-8c37-4d65-adee-cf1acfcfc5fd.apk")
    #     sleep(5)
    @data(*excel.getDataFromSheet())
    def test_select_app(self,data):
        LoginPage(self.driver, data['username'], data['password']).Login()

        HomePage_one(self.driver).choise_project()
        HomePage_one(self.driver).appmanage()
        # 打印当前页面所有的url
        Get_curr_alllink(self.driver).PrintLink()

        sleep(3)
        AppMangerPage(self.driver).selectByAppName("熊猫直播")
        Get_curr_alllink(self.driver).PrintLink()




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