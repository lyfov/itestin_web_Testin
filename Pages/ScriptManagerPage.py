from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class ScriptManagerPage(Page):
    script_group_loc_tab=(By.XPATH,"//li/a[contains(text(),'脚本组')]")
    creat_scrpt_group_loc=(By.XPATH,"//div/button[contains(text(),'创建脚本组')]")
    #脚本描述文本输入框的定位器
    group_description_loc=(By.ID,"modifyGroupDesc")
    #点击第一个脚本后面的添加按钮定位器
    add_script_loc=(By.XPATH,'//*[@id="dialogTable"]/tbody/tr[2]/td[7]/a[1]')




    def __init__(self, driver):
        self.driver = driver
        # self.driver=webdriver.Chrome()
        print("脚本页面打开成功")
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
            self.driver.find_element(*self.group_description_loc).send(value)
        except NoSuchElementException as e:
            print("未找到脚本描述输入框")
    #点击第一个脚本的添加按钮
    def add_button_twice(self):
        try:
            self.driver.find_element(*self.add_script_loc).send()
            self.driver.find_element(*self.add_script_loc).send()
        except NoSuchElementException as e:
            print("未找到脚本的添加按钮")