from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Onlinepage(Page):
    save_loc=(By.XPATH,'//*[contains(text(),"保存")]')
    wait_loc = (By.XPATH,'//dl/dd[contains(text(),"等待")]')
    wait_for_wait_loc = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/button/span/ul/li/div/ul/li[1]')
    sure_loc = (By.XPATH,'//*[contains(text(),"确 定")]')
    app_aline_loc =(By.XPATH,'//*[@id="app"]/div[11]/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div/div/label/span[1]/span')
    app_sure_loc = (By.XPATH,'//*[@id="app"]/div[11]/div/div[3]/div/button[2]/span')
    input_script_loc = (By.XPATH,'//*[@id="app"]/div[3]/div/div/div[2]/form/div[1]/div/div/input')
    scrpit_save_sure = (By.XPATH,'//*[@id="app"]/div[3]/div/div/div[3]/div/button[2]')
    update_sure_loc=(By.XPATH,'//*[@id="app"]/div[7]/div/div[3]/div/button[2]/span')

    def __init__(self,driver):
        self.driver=driver
        print("首页初始化完成")

    #点击保存按钮
    def click_Save(self):
        try:
            sleep(3)
            self.element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(self.save_loc))
            self.element.click()
        except NoSuchElementException:
            print("未找到保存按钮")

        # 点击等待按钮
    def click_Wait(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.wait_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到等待按钮")

            #点击等待下拉框的等待
    def click_WaitForWait(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.wait_for_wait_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到等待下拉框中的等待按钮")
        #点击确认按钮
    def click_Makesure(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.sure_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到确认按钮")

        #点击应用的单选框
    def click_app_choose(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(self.app_aline_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到确认按钮")

        # 点击应用的确认按钮
    def click_app_sure(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.app_sure_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到确认按钮")
        #输入脚本描述
    def input_script_text(self,value="自动化创建的脚本"):
            try:
                self.element = WebDriverWait(self.driver, 10, 0.5).until(
                    EC.presence_of_element_located(self.input_script_loc))
                self.element.send_keys(value)
            except NoSuchElementException as c:
                print("未找到确认按钮")

        #输入脚本描述
    def click_script_Makesure(self):
            try:
                self.element = WebDriverWait(self.driver, 10, 0.5).until(
                    EC.presence_of_element_located(self.scrpit_save_sure))
                self.element.click()
            except NoSuchElementException as c:
                print("未找到确认按钮")
            # 点击更新描述的保存

    def click_updata_Makesure(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.update_sure_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到确认按钮")