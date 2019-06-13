from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class ScriptManagerPage(Page):
    script_group_loc_tab=(By.XPATH,"//li/a[contains(text(),'脚本组')]")
    creat_scrpt_group_loc=(By.XPATH,"//div/button[contains(text(),'创建脚本组')]")
    #已添加按钮
    added_script_loc=(By.XPATH,'//*[@id="saveScriptGroup-form"]/ul/li/button[2]')
    #脚本描述文本输入框的定位器
    group_description_loc=(By.ID,"modifyGroupDesc")
    #点击第一个脚本后面的添加按钮定位器
    add_script_loc=(By.XPATH,'//*[@id="dialogTable"]/tbody/tr[2]/td[7]/a[1]')
    #点击全选清除数据按钮
    allclear_data_loc=(By.XPATH,'//*[@id="saveScriptGroup-form"]/div/ul/li[1]/span[2]/span[1]/label/span')
    #弹窗的创建按钮
    creat_succesful_loc=(By.XPATH,'//div/button[text()="创建" and @type="button"]')
    #脚本组中第一个脚本组的修改按钮
    update_one_loc=(By.XPATH,'//*[@id="mainTable"]/tbody/tr[2]/td[7]/a[2]')
    #修改弹层中的修改确认按钮
    update_success_loc=(By.XPATH,'//div/button[text()="修改" and @type="button"]')
    #第一个脚本组的删除按钮
    delete_group_first_loc=(By.XPATH,'//*[@id="mainTable"]/tbody/tr[2]/td[7]/a[1]')
    #删除的确认按钮
    delete_confirm_loc=(By.XPATH,'//button[text()="确认"]')
    def __init__(self, driver):
        self.driver = driver
        # self.driver=webdriver.Chrome()

        # print(self.driver.find_element(*self.first_upload_loc).is_displayed())

    #点击脚本组tab
    def click_scrpt_group_tab(self):
        try:
            self.driver.find_element(*self.script_group_loc_tab).click()
        except NoSuchElementException as e:
            print("未找到脚本组tab页按钮")
    # 点击脚本组tab
    def click_creat_scrpt_group(self):
        try:
            self.driver.find_element(*self.creat_scrpt_group_loc).click()
        except NoSuchElementException as e:
            print("未找到创建脚本组按钮")
    #文本输入框输入脚本组名称
    def input_description_value(self,value):
        try:
            self.driver.find_element(*self.group_description_loc).send_keys(value)
        except NoSuchElementException as e:
            print("未找到脚本描述输入框")
    #点击第一个脚本的添加按钮
    def add_button_twice(self):
        try:
            self.driver.find_element(*self.add_script_loc).click()
            sleep(3)
            self.driver.find_element(*self.add_script_loc).click()
        except NoSuchElementException as e:
            print("未找到脚本的添加按钮")
        # 点击第一个脚本的添加按钮

    def click_added(self):
        try:
            self.driver.find_element(*self.added_script_loc).click()

        except NoSuchElementException as e:
            print("未找到已添加按钮")
        # 点击全选清除数据按钮

    def click_ALL_clear(self):
        try:
            self.driver.find_element(*self.allclear_data_loc).click()
            if self.driver.find_element(*self.allclear_data_loc).is_selected():
                print("清除按钮点击完毕")
        except NoSuchElementException as e:
            print("未找到已添加按钮")
    #点击弹窗的创建按钮
    def click_success_creat(self):
        print("========>>>>>>等待点击弹窗的创建按钮")
        self.element=WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(self.creat_succesful_loc))
        self.element.click()
    #得到当前页面的弹窗信息
    def Get_Alert_message(self):
        sleep(3)
        # self.driver=webdriver.Chrome()
        w = self.driver.switch_to_alert()
        text=w.text
        sleep(3)
        w.accept()
        return text
        # 点击弹窗的创建按钮
    #点击第一个脚本的修改按钮
    def click_first_updata(self):
        print("========>>>>>>等待点击第一个脚本的修改按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.update_one_loc))
        self.element.click()

        # 点击第一个脚本的修改按钮

    def click_upadata_success(self):
        print("========>>>>>>等待点击第一个脚本的修改按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.update_success_loc))
        self.element.click()
        #点击第一个脚本组的删除按钮
    def click_Delete_Forst(self):
        print("========>>>>>>等待点击第一个脚本组的删除按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.delete_group_first_loc))
        self.element.click()
       #点击删除确认按钮
    def click_Remove_Confirm(self):
        print("========>>>>>>等待点击删除确认按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.delete_confirm_loc))
        self.element.click()
