from common.BasePage import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Onlinepage(Page):
    wait_loc=(By.XPATH,'//*[@id="app"]/header/div[1]/div/div[1]/ul/li[1]/div')


    def __init__(self,driver):
        self.driver=driver
        print("首页初始化完成")

    #点击等待
    def click_Wait(self):
        self.element = WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(self.wait_loc))
        self.element.click()

