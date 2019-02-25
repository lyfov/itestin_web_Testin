from common.BasePage import Page
from selenium.webdriver.common.by import By
from time import sleep


class LoginPage(Page):

    #登录页面的所有属性及定位器
    username_loc=(By.ID,'email')
    pwd_loc=(By.ID,'pwd')
    submitBtn_loc=(By.ID,'submitBtn')

    #输入用户名
    def input_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)
        sleep(1)
    #输入密码
    def input_pwd(self,pwd):
        self.find_element(*self.pwd_loc).clear()
        self.find_element(*self.pwd_loc).send_keys(pwd)

        sleep(1)
    #点击登录按钮
    def click_buttonforlogin(self):
        self.find_element(*self.submitBtn_loc).click()
    #登录功能所有操作，其他用例可以直接执行
    def Login(self,username="chenhaodong@testin.cn",pwd="123456"):
        log=LoginPage(self.driver)
       # print(os.getpid())
        log.open()
        #print(os.getpid())
        log.input_username(username)
        log.input_pwd(pwd)
        log.click_buttonforlogin()
        sleep(3)

