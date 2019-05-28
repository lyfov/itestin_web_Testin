from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
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


        except:
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


        # WebDriverWait(self.driver,100).until(lambda s:s.find_element(*self.button_sub_loc))


