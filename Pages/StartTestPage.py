from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.BasePage import Page


class StartTestPage(Page):

    Start_Test_loc=(By.XPATH,'//*[@id="showTaskList"]/div[1]/div/button')
    choose_app_input_loc=(By.XPATH,'//*[@id="appSelect-form"]/div[1]/div[1]/div/button/span[1]')
    chosse_wuxianji_loc = (By.XPATH, "//a/span[contains(text(),'无限极中国')]")
    query_app_loc=(By.XPATH,'//*[@id="search"]')
    list_wuxianji_loc =(By.XPATH,'//*[@id="content"]/table/tbody/tr[2]/td[1]')
    next_step_loc=(By.XPATH,'//*[contains(text(),"下一步")]')
    add_script_loc=(By.XPATH,'//*[@id="content"]/div[3]/div[1]/table/tbody/tr[2]/td[8]/a[1]')
    devices_all_loc=(By.XPATH,'//*[@id="select_device_form"]/div/div[2]/div[1]/div[1]/button[1]')
    task_name_loc=(By.XPATH,'//*[@id="descr"]')
    # devices_next_loc=(By.XPATH,'//*[@id="select_device_form"]/div/div[2]/div[3]/div/button[2]')
    # 设备的下一步按钮
    devices_next_loc=(By.CSS_SELECTOR,'#select_device_form > div > div.panel.panel-default.grid-device > div.page-operation-bar.fix > div > button.btn.btn-primary.nextStep')
    subtest_loc=(By.XPATH,'/html/body/div[1]/div[4]/div/button[2]')
    # 提测成功后查看任务按钮
    check_task_loc = (By.XPATH, '//div/a[contains(text(),"查看任务")]')




    def __init__(self,driver):
        self.driver = driver
        print("自动化功能提测页面展示成功")

    #click startTest button
    def click_StartTest_button(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.Start_Test_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("aaaa")
     #choose app is wuxianji
    def choose_app_wuxianji(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.choose_app_input_loc))
            self.element.click()
            print("输入选择app成功")
        except NoSuchElementException as c:
            print("aaaa")
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.chosse_wuxianji_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到无限极")
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.query_app_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到查询按钮")

        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.list_wuxianji_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到查询按钮")

    def click_next_step(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.next_step_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("下一步")

    def add_script(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.add_script_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("添加按钮未找到")

    def add_devices_all(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.devices_all_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到添加全部按钮")

        sleep(3)

    def input_test_name(self,value="测试任务"):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.task_name_loc))
            self.element.send_keys(value)
        except NoSuchElementException as c:
            print("未找到输入框")
    def click_device_next(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.devices_next_loc))
            self.element.click()
            # self.driver = webdriver.Chrome()

        except NoSuchElementException as c:
            print("未找到输入框")

    def click_subtest(self):
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.subtest_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("提交测试按钮")
        sleep(3)

    def click_check_task(self):
        print("=========任务提交成功=======")
        try:
            self.element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located(self.check_task_loc))
            self.element.click()
        except NoSuchElementException as c:
            print("未找到查看任务按钮")
