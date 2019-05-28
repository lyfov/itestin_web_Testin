from common.BasePage import Page
from selenium.webdriver.common.by import By
from time import sleep
from common.ExcelUtil import ParseExcel
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
class LoginPage(Page):
    # excel = ParseExcel("C:\\Users\\HP\\Desktop\\1.xlsx","Sheet1")

    #登录页面的所有属性及定位器
    username_loc=(By.ID,'email')
    pwd_loc=(By.ID,'pwd')
    submitBtn_loc=(By.ID,'submitBtn')

    def __init__(self,driver,username,pwd):
        self.username =username
        self.pwd = pwd
        self.driver =driver

    #输入用户名
    def input_username(self):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(self.username)
        sleep(1)
    
    #输入密码
    def input_pwd(self):
        self.find_element(*self.pwd_loc).clear()
        self.find_element(*self.pwd_loc).send_keys(self.pwd)

        sleep(1)
    #点击登录按钮
    def click_buttonforlogin(self):
        self.find_element(*self.submitBtn_loc).click()



    #判断提示信息是否存在在页面上

    def check_tagmessage(self,tagmessage):
        # self.driver = webdriver.Chrome()

        xpath_current = '//*[contains(text(),"'+ tagmessage +'")]'
        print(xpath_current)
        try:
         self.driver.find_element_by_xpath(xpath_current)
        except NoSuchElementException as e:
         print("未找到"+tagmessage+"提示信息")
    #登录功能所有操作，其他用例可以直接执行
    def Login(self,):
        log=LoginPage(self.driver,self.username,self.pwd)
       # print(os.getpid())
        log.open()
        #print(os.getpid())
        log.input_username()
        log.input_pwd()
        log.click_buttonforlogin()



