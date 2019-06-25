from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
class AppMangerPage(Page):
    first_upload_loc =(By.XPATH,'//span/a[contains(text(),"上传应用")]')
    second_upload_loc=(By.XPATH,'//button[contains(text(),"上传应用")]')
    button_sub_loc=(By.XPATH,'//div/button[contains(text(),"提交")]')
    name_select_loc=(By.XPATH,'//button/span[contains(text(),"请选择应用名称")]')
    name_input_loc=(By.XPATH,'//*[@id="search-form"]/div[1]/div/div/div/input')
    name_text_loc=(By.XPATH,'//*[@id="search-form"]/div[1]/div/div/ul/li[2]/a/span[1]')
    w=(By.CLASS_NAME,'page-main')
    jqurey_button_loc=(By.XPATH,'//button[contains(text(),"查询")]')
    APPDELETE_True_loc=(By.XPATH,'//button[contains(text(),"确认")]')
    appback_loc=(By.XPATH,'//*[@id="page-menu"]/div/nav/div/ul/li[1]/a/span')
    dowlond_loc=(By.XPATH,'//*[@id="cp_quota"]/div/table/tbody/tr[2]/td[8]/a[1]')
    #测试记录按钮
    testnode=(By.XPATH,'//*[@id="cp_quota"]/div/table/tbody/tr[2]/td[8]/div/a')

    #功能测试
    testbode_gongneng=(By.XPATH,'//*[@id="cp_quota"]/div/table/tbody/tr[2]/td[8]/div/ul/li[1]/a')
    #兼容测试
    testbode_jianrong = (By.XPATH, '//*[@id="cp_quota"]/div/table/tbody/tr[2]/td[8]/div/ul/li[2]/a')

    #云监控测试
    testbode_yunjiankong = (By.XPATH, '//*[@id="cp_quota"]/div/table/tbody/tr[2]/td[8]/div/ul/li[3]/a')
    def __init__(self, driver):
        self.driver = driver
        # self.driver=webdriver.Chrome()
        print("应用管理页面加载完成")
        # print(self.driver.find_element(*self.first_upload_loc).is_displayed())
    #点击上传按钮
    def upload_click(self):
        sleep(3)
        # 点击上传按钮的超链接
        # print(self.driver.find_element(*self.first_upload_loc).is_displayed())
        try:
            self.driver.find_element(*self.first_upload_loc).is_displayed()
            self.find_element(*self.first_upload_loc)
        except NoSuchElementException as e:
            print("没找到超链接元素")
        finally:
            #点击右上角上传
            self.driver.find_element(*self.second_upload_loc).click()

    #上传选定的文件
    def upload_app_byname(self,filename):

        # self.driver=webdriver.Chrome()
        self.driver.find_element_by_name("file").send_keys(filename)

        WebDriverWait(self.driver,100).until(lambda s:s.find_element(*self.button_sub_loc))
    #点击查询按钮


    #筛选功能
    def selectByAppName(self,name="熊猫直播"):
        sleep(3)
        self.find_element(*self.name_select_loc).click()
        sleep(3)
        self.find_element(*self.name_input_loc).send_keys(name)
        sleep(3)
        self.clickEnterNoElement()
        self.find_element(*self.jqurey_button_loc).click()
        return 1
    def DeleteApp(self,name=""):
        xpath = "//a[contains(@app-name,'" + name +"')]"
        self.find_element(By.XPATH,xpath).click()
        print(xpath)
        sleep(5)
        self.find_element(*self.APPDELETE_True_loc).click()
        sleep(5)
     #获得弹出框的文本信息
    def Get_Alert_message(self):

        # self.driver=webdriver.Chrome()
        w= self.driver.switch_to_alert().text
        return w
        #点击左上角应用管理，回到应用管理页面
    def click_back_APPmanage(self):

        self.find_element(*self.appback_loc).click()


    #click download button

    def click_test_node(self):

        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.dowlond_loc))
        self.element.click()
    #点击记录中功能测试

    def click_node_gongneng(self):
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.testbode_gongneng))
        self.element.click()
        # 点击记录中兼容测试

    def click_node_jianrong(self):
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.testbode_jianrong))
        self.element.click()

    # 点击记录中云监控测试

    def click_node_yunjiankong(self):
        self.element = WebDriverWait(self.driver, 10, 0.5).until(
            EC.presence_of_element_located(self.testbode_yunjiankong))
        self.element.click()
