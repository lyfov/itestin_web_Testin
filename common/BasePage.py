from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from TestLogger import TestLogger
import os
class Page(object):
    logs =TestLogger(os.getcwd()).console_log()
    #初始化driver
    def __init__(self,driver):
        # self.url="http://test.pro.testin.cn/account/login.htm"
        self.driver = driver


       # self.driver =webdriver.Chrome()
    #封装打开网页功能
    def open(self):
        self.driver.get("http://test.pro.testin.cn/account/login.htm")
        self.driver.maximize_window()
    # 封装定位器查找元素功能
    def find_element(self,*loc):
        return self.driver.find_element(*loc)


    #判断元素是否再当前页面
    def element_on_current(self,by,value):
        try:
            element=self.driver.find_element(by=by,value=value)
        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True

     #鼠标移动到对应xpath位置并右键点击
    def move_mouse_to_xpath(self,xpath):
        try:
            ActionChains(self.driver).context_click(self.driver.find_element_by_xpath(xpath)).perform()
        except:
            print("未找到元素，右键点击失败")
        pass

    #选择下拉列表的元素,value代表文案内容，如value="xxxxx"
    def select_value_xpath(self,value):
        # xpath ="//form/ui/li[@title='"+value+"']"
        try:
            # element = self.driver.find_element_by_xpath(xpath)
            element = self.driver.find_element_by_xpath(value)
            element.click()
            # self.logs.info("asdsadasdsadsadsad")
        except NoSuchElementException as e:
            print("未找到对应的 %S" %value)