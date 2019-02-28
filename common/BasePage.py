from selenium.common.exceptions import NoSuchElementException
from common.TestLogger import TestLogger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os
class Page(object):
    #print("-------------------------------"+os.getcwd())
    w=r"C:\Users\HP\PycharmProjects\itestin_web_tencent\logs"
   # print(w)
    logs =TestLogger(w).console_log()
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
            print("未找到对应的 %s" %value)
    # 模拟键盘回车操作
    def keys_enter_element(self,by,value):
        try:
            element = self.driver.find_element(by=by, value=value)
            element.send_keys(Keys.ENTER)
        except NoSuchElementException as e:
            print("未找到对应的%s" %value)

    # 模拟键盘复制操作
    def keys_ctrl_c_element(self,by,value):
        try:
            element = self.driver.find_element(by=by, value=value)
            element.send_keys(Keys.CONTROL,'c')
        except NoSuchElementException as e:
            print("未找到对应的%s" %value)

     # 模拟键盘粘贴操作
    def keys_ctrl_v_element(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
            element.send_keys(Keys.CONTROL,'v')
        except NoSuchElementException as e:
            print("未找到对应的%s" % value)

        # 模拟键盘剪切操作
    def keys_ctrl_x_element(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
            element.send_keys(Keys.CONTROL,'x')
        except NoSuchElementException as e:
            print("未找到对应的%s" % value)

     # 模拟键盘全选操作
    def keys_ctrl_a_element(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
            element.send_keys(Keys.CONTROL,'a')
        except NoSuchElementException as e:
            print("未找到对应的%s" % value)
    # 模拟键盘TAB操作
    def keys_ctrl_TAB_element(self, by, value):
        try:
            element = self.driver.find_element(by=by, value=value)
            element.send_keys(Keys.TAB)
        except NoSuchElementException as e:
            print("未找到对应的%s" % value)


    # 模拟鼠标操作
    #模拟鼠标右键
    def context_click_element(self, by, value):
            try:
                element = self.driver.find_element(by=by, value=value)
                ActionChains(self.driver).context_click(element).perform()
            except NoSuchElementException as e:
                print("未找到对应的%s" % value)



        #鼠标再元素上悬停
    def move_to_element(self, by, value):
            try:
                element = self.driver.find_element(by=by, value=value)
                ActionChains(self.driver).move_to_element(element).perform()
            except NoSuchElementException as e:
                print("未找到对应的%s" % value)

    #双击鼠标
    def double_element(self, by, value):
            try:
                element = self.driver.find_element(by=by,value=value)
                ActionChains(self.driver).double_click(element).perform()
            except NoSuchElementException as e:
                print("未找到%s" %value)