from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage_one(Page):
    #项目组列表下拉按钮属性
    project_loc=(By.CLASS_NAME,"dropdown-btn")
    #要选择的项目组的xpath
    toprject_loc ='//*[@id="page-menu"]/div/nav/div/div/div/div/div/form/ul/li[1]'
    #应用管理loc
    appmanage_loc =(By.XPATH,'//span[contains(text(),"应用管理")]')
    #自动化管理定位器
    auto_manager_loc=(By.XPATH,'//*[@id="page-menu"]/div/nav/div/ul/li[3]/a/span')
    #脚本管理定位器
    scripy_home_loc=(By.XPATH,'//*[@id="page-menu"]/div/nav/div/ul/li[3]/ul/li/a')
    # 录制脚本按钮
    recordingBtn_loc = (By.XPATH, '//button[text()="录制脚本"]')
    test_manage_loc=(By.XPATH,'//*[@id="page-menu"]/div/nav/div/ul/li[2]/a/span')
    test_for_gn_loc=(By.XPATH,'//*[@id="page-menu"]/div/nav/div/ul/li[2]/ul/li[1]/a')

    #功能tab页面的元素定位器
    appname_loc = (By.XPATH,'//*[@id="auto_list"]/div[1]/div/button/span[1]')
    app_one_loc =(By.XPATH,'//*[@id="auto_list"]/div[1]/div/div/ul/li[2]/a/span[1]')
    dingshirenwu_loc=(By.XPATH,'//*[@id="showTaskList"]/div[2]/ul/li[2]/a')

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
    #点击脚本管理
    def click_auto_script(self):
        self.driver.find_element(*self.auto_manager_loc).click()

        sleep(2)

        self.driver.find_element(*self.scripy_home_loc).click()
     #点击录制脚本
    def click_recordingBtn(self):
        print("========>>>>>>等待点击录制脚本按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.recordingBtn_loc))
        self.element.click()
    #点击测试管理

    def click_TestManage(self):
        sleep(3)
        print("========>>>>>>等待点击测试管理按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.test_manage_loc))
        self.element.click()
        # 点击功能测试

    def click_gongneng(self):
        sleep(3)
        print("========>>>>>>等待点击功能测试按钮")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.test_for_gn_loc))
        self.element.click()

        #点击应用名称
    def click_appname(self):
        sleep(3)
        print("========>>>>>>等待点击应用名称")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.appmanage_loc))
        self.element.click()
        #点击第一个应用名称
    def click_appnameone(self):
        sleep(3)
        print("========>>>>>>等待点击第一个应用")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.app_one_loc))
        self.element.click()
        #点击定时任务
    def click_dingshirenwu(self):
        sleep(3)
        print("========>>>>>>等待点击第一个应用")
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.dingshirenwu_loc))
        self.element.click()