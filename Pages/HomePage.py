from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


class HomePage_one(Page):
    #项目组列表下拉按钮属性
    project_loc=(By.CLASS_NAME,"dropdown-btn")
    #要选择的项目组的xpath
    toprject_loc ='//*[@id="page-menu"]/div/nav/div/div/div/div/div/form/ul/li[1]'
    #应用管理loc
    appmanage_loc =(By.XPATH,'//span[contains(text(),"应用管理")]')


    def __init__(self,driver):
        self.driver=driver
        print("首页初始化完成")
    #点击出现项目的下拉按钮
    def click_project(self):
        element=self.find_element(*self.project_loc)
        print("找到按钮了")
        element.click()
    def get_current_url(self):
        self.driver.getcurrent_url()
    #切换目标的项目组
    def choise_project(self):
        self.click_project()
        print("-------")
        self.select_value_xpath(self.toprject_loc)

    #点击应用管理
    def appmanage(self):
        try:
            sleep(5)
            #element = WebDriverWait(self.driver,10).until(self.driver.find_element(*self.appmanage_loc))
            #print(lambda driver:self.find_element(*self.appmanage_loc)

            element=self.find_element(*self.appmanage_loc)
            sleep(5)
            element.click()
            print("点击完成")
            print(self.getcurrent_url())
        except NoSuchElementException as e:
            print("未找到元素 应用管理")





