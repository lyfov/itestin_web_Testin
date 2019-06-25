from common.BasePage import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class ManagePage(Page):
    rukou_loc=(By.XPATH,'//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[2]/a/span')
    #点击查看详情连接
    xiangqing_loc=(By.XPATH,'//*[@id="page-body"]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/a')
    creat_project_loc=(By.XPATH,'//*[@id="page-body"]/div[2]/div[1]/div/button')
    #input projectname
    name_loc=(By.XPATH,'//*[@id="add_project_name"]')
    #取消按钮
    quit_creat_loc=(By.XPATH,'//*[@id="modal_project_create"]/div/div/div[3]/button[1]')

    #确认按钮
    true_creat_loc=(By.XPATH,'//*[@id="modal_project_create"]/div/div/div[3]/button[2]')


    def __init__(self,driver):
        self.driver=driver
        print("首页初始化完成")

    #点击管理中心按钮
    def click_comein(self):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(self.rukou_loc))
            self.element.click()
        except NoSuchElementException:
            print("未找到管理按钮")

        # 点击项目概况的查看详情

    def click_chakanxiangqing_project(self):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.xiangqing_loc))
            self.element.click()
        except NoSuchElementException:
            print("查看详情连接")




   # 点击创建项目组

    def click_creat_project(self):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.creat_project_loc))
            self.element.click()
        except NoSuchElementException:
            print("未找到创建项目组按钮")

        # 输入项目名称

    def input_project_name(self,value="新创建的项目组"):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.name_loc))
            self.element.send_keys(value)
        except NoSuchElementException:
            print("名称输入框")

        # 点击取消创建按钮
    def click_quit_creat(self):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.quit_creat_loc))
            self.element.click()
        except NoSuchElementException:
            print("未找到取消按钮")

        # 点击确定创建按钮
    def click_true_creat(self):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.true_creat_loc))
            self.element.click()
        except NoSuchElementException:
            print("未找到确认按钮")


    #得到控件的文本信息

    def get_text_button(self,xpath):
        text=self.driver.find_element_by_xpath(xpath).text
        return text