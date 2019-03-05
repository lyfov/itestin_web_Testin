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
