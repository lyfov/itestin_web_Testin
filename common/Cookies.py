from selenium import webdriver
from time import sleep
import _so

class Cookies_private():

    def getCookies(self):
        self.driver=webdriver.Chrome(r'C:\Users\HP\Downloads\chromedriver_win32 (4)\chromedriver.exe')
        self.driver.get("http://test.pro.testin.cn/account/login.htm")
        print(self.driver.get_cookies())

        sleep(3)
        self.driver.find_element_by_id("email").send_keys("chenhaodong@testin.cn")
        sleep(3)
        self.driver.find_element_by_id("pwd").send_keys("123456")
        sleep(3)
        self.driver.find_element_by_id("submitBtn").click()
        print(self.driver.get_cookies())


if __name__=="__main__":
    # print(Cookies_private(webdriver.Chrome()).getCookies())
    # Cookies_private(webdriver.Chrome(r'C:\Users\HP\Downloads\chromedriver_win32 (4)\chromedriver.exe'))
    #
    # Cookies_private(webdriver.Chrome()).get("http://test.pro.testin.cn/account/login.htm")
    # Cookies_private(webdriver.Chrome()).getCookies()
    # print(Cookies_private(webdriver.Chrome()).getCookies())
    Cookies_private().getCookies()









    pass